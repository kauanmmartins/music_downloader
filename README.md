# YouTube to MP3 Downloader 🎵

A simple and efficient Python script to download audio from YouTube videos and automatically convert them to high-quality MP3 format.

## Features

- **Audio-only download:** Saves time and data by fetching only the audio stream.
- **Accepts multiple links:** You can download a list of videos if you want.
- **Automatic Conversion:** Converts files to `.mp3` seamlessly using FFmpeg.
- **Auto-naming:** Files are automatically named based on the YouTube video title.
- **Up-to-date:** Powered by `yt-dlp` to ensure compatibility with the latest YouTube updates.

## Prerequisites

Before running the script, ensure you have the following installed:

1.  **Python 3.x**
2.  **FFmpeg**: Essential for audio conversion.
    - *Tip:* Make sure FFmpeg is added to your system's PATH.
3.  **Node.js** (Optional but recommended): Helps the script handle YouTube's JavaScript-based protections.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)

2. Navigate to the project folder:
    cd YOUR_REPOSITORY_NAME

3. Install the required library:
    pip install yt-dlp

4. Run the script:
    python baixar_musica.py
