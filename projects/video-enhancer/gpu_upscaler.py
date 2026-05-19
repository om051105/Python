import cv2
import torch
import sys
import os
import numpy as np
from tqdm import tqdm
from super_image import EdsrModel, ImageLoader
from PIL import Image

def upsale_video_gpu(input_path, output_path, scale=4):
    print(f"Checking GPU availability...")
    if not torch.cuda.is_available():
        print("❌ WARNING: CUDA (NVIDIA GPU) is NOT detected by PyTorch.")
        print("This script will run on CPU, which is very slow.")
        print("If you have an RTX card, ensure you installed the CUDA version of PyTorch.")
        device = 'cpu'
    else:
        print(f"✅ GPU Detected: {torch.cuda.get_device_name(0)}")
        device = 'cuda'

    # Load Model (EDSR)
    # Different models can be used: 'eugenesiow/edsr-base', 'eugenesiow/espcn', etc.
    # We will use EDSR-base as it offers a good balance.
    model_name = 'eugenesiow/edsr-base'
    
    print(f"Loading AI Model ({model_name}) to {device}...")
    try:
        model = EdsrModel.from_pretrained(model_name, scale=scale)
        model.to(device)
        model.eval()
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # Open Video
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    new_width = width * scale
    new_height = height * scale
    
    print(f"Input Resolution: {width}x{height}")
    print(f"Processing Resolution: {new_width}x{new_height} (Internal)")
    print(f"Output Resolution: {width}x{height} (Original)") # We are keeping original
    print(f"FPS: {fps}")

    # Video Writer - Save at ORIGINAL resolution
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    print("Starting GPU Enhancement (Upscale + Refine)...")
    
    # Process Frames
    pbar = tqdm(total=total_frames, unit='frame')
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Convert OpenCV (BGR) to PIL (RGB)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            inputs = ImageLoader.load_image(Image.fromarray(frame_rgb))
            inputs = inputs.to(device)

            # Upscale
            with torch.no_grad():
                preds = model(inputs)
            
            output_tensor = preds.data.cpu().squeeze(0)
            output_tensor = output_tensor.mul(255).clamp(0, 255).byte().permute(1, 2, 0).numpy()
            output_bgr = cv2.cvtColor(output_tensor, cv2.COLOR_RGB2BGR)

            # Downscale back to original resolution using High Quality interpolation
            # This preserves the added details from the AI but keeps file size/resolution manageable
            enhanced_frame = cv2.resize(output_bgr, (width, height), interpolation=cv2.INTER_AREA)

            out.write(enhanced_frame)
            pbar.update(1)
            
    except KeyboardInterrupt:
        print("\nStopped by user.")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        cap.release()
        out.release()
        pbar.close()
        print(f"\nFinished. Saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gpu_upscaler.py <video_path>")
        file_path = input("Enter video path: ").strip().strip('"').strip("'")
    else:
        file_path = sys.argv[1].strip().strip('"').strip("'")
    
    if not os.path.exists(file_path):
        print("File not found.")
        sys.exit(1)

    filename, ext = os.path.splitext(file_path)
    output_path = f"{filename}_enhanced{ext}"
    
    # We upscale 2x internally to generate detail, then downscale back
    upsale_video_gpu(file_path, output_path, scale=2)
