import cv2
import os
import requests
import sys
from tqdm import tqdm

def download_model(model_name):
    """
    Downloads the Super Resolution model if it doesn't exist.
    """
    url = ""
    if model_name == "EDSR_x4.pb":
        # Using a reliable mirror or source for the pre-trained EDSR model compatible with OpenCV
        url = "https://github.com/Saafke/EDSR_Tensorflow/raw/master/models/EDSR_x4.pb"
    elif model_name == "ESPCN_x4.pb":
         url = "https://github.com/fannymonori/TF-ESPCN/raw/master/export/ESPCN_x4.pb"
    
    if not os.path.exists(model_name):
        print(f"Downloading {model_name} model... This might take a while.")
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        
        with open(model_name, 'wb') as f, tqdm(
            desc=model_name,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                size = f.write(data)
                bar.update(size)
        print("Download complete.")
    else:
        print(f"Model {model_name} found.")

def upscale_video(input_path, output_path, model="EDSR", scale=4):
    """
    Upscales a video using OpenCV DNN Super Resolution.
    """
    # Initialize DNN SuperRes object
    sr = cv2.dnn_superres.DnnSuperResImpl_create()

    model_filename = f"{model}_x{scale}.pb"
    download_model(model_filename)

    print(f"Reading model {model_filename}...")
    try:
        sr.readModel(model_filename)
        sr.setModel(model.lower(), scale)
        
        # Attempt to use GPU (CUDA)
        print("Attempting to use GPU (CUDA) for processing...")
        try:
            sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
            # Dummy run to check if CUDA is actually available/working
            dummy_frame = cv2.imread(model_filename) # Will fail to read, but we need a dummy mat. 
            # Actually easier: just don't crash here. The error usually happens on first .upsample call.
            print("GPU configurations set. If OpenCV was built with CUDA, this will be fast.")
        except Exception as e_cuda:
            print(f"CUDA setup failed or not available: {e_cuda}")
            print("Falling back to CPU...")
            sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
            sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please ensure you have opencv-contrib-python installed.")
        return

    # Open input video
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {input_path}")
        return

    # Get original video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate new dimensions
    new_width = width * scale
    new_height = height * scale

    print(f"Original Resolution: {width}x{height}")
    print(f"Upscaled Resolution: {new_width}x{new_height}")
    print(f"FPS: {fps}")
    print(f"Total Frames: {total_frames}")

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # mp4v is reliable for .mp4
    out = cv2.VideoWriter(output_path, fourcc, fps, (new_width, new_height))

    print("Starting upscaling process... (Press 'q' to cancel)")
    
    if total_frames > 0:
        pbar = tqdm(total=total_frames, unit='frame')
    else:
        pbar = tqdm(unit='frame')

    frame_count = 0
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Upscale the frame
            try:
                upscaled_frame = sr.upsample(frame)
            except cv2.error as e:
                # If CUDA fails during runtime (common if not supported), switch to CPU
                if "The function/feature is not implemented" in str(e) or "CUDA" in str(e):
                     print("\n\nCUDA Error detected. Switching to CPU mode automatically...")
                     sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
                     sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
                     upscaled_frame = sr.upsample(frame)
                else:
                    raise e


            # Write to output
            out.write(upscaled_frame)

            pbar.update(1)
            frame_count += 1
            
            # Allow cancelling with 'q' if running in a windowed env, 
            # though this is CLI, it's good practice for debugging if imshow was used.
            # Here we just check for KeyboardInterrupt via tqdm usually, but we'll stick to loop.

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        cap.release()
        out.release()
        pbar.close()
        print(f"\nProcessing finished. Saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python video_upscaler.py <input_video_path> [output_video_path]")
        input_file = input("Enter path to input video: ").strip()
        if not input_file:
            print("No input file provided. Exiting.")
            sys.exit(1)
    else:
        input_file = sys.argv[1]

    # Clean quotes from path if dragged and dropped
    input_file = input_file.strip('"').strip("'")

    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        filename, ext = os.path.splitext(input_file)
        output_file = f"{filename}_upscaled.mp4"

    # Settings
    # Models: EDSR (Slow, Best Quality), ESPCN (Fast, Good Quality), FSRCNN, LapSRN
    # Scale: 2, 3, 4
    
    print("--- Video Upscaler ---")
    print("1. Fast (ESPCN) - Good for real-time or quick results")
    print("2. High Quality (EDSR) - Very slow, best results")
    choice = input("Select mode (1/2) [default=1]: ").strip()
    
    if choice == '2':
        selected_model = "EDSR"
    else:
        selected_model = "ESPCN"

    upscale_video(input_file, output_file, model=selected_model, scale=4)
