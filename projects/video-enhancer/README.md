# AI Video Upscaler

This tool uses Deep Learning models to increase the resolution and quality of your videos.

## Features
- **AI Upscaling**: Uses state-of-the-art super-resolution models (EDSR and ESPCN).
- **Automatic Model Download**: No need to manually find model files; the script downloads them for you.
- **Simple Usage**: clear command-line interface.

## Prerequisites
- Python 3.x
- Dependencies (installed via `pip install -r requirements.txt`)

## How to Run

1.  Open your terminal in this folder.
2.  Run the script:
    ```bash
    python video_upscaler.py
    ```
3.  Follow the prompts:
    -   Enter the path to your video file (you can drag and drop the file into the terminal).
    -   Select the quality mode:
        -   **Mode 1 (Fast)**: Uses the ESPCN model. Good for real-time upsizing and general enhancement.
        -   **Mode 2 (High Quality)**: Uses the EDSR model. This provides the best quality but is significantly slower.

## Note on Performance
-   **EDSR (High Quality)** is computationally expensive. Upscaling even a short video might take a significant amount of time depending on your CPU/GPU.
-   The output video will be saved in the same directory as the input video with `_upscaled` appended to the filename.
