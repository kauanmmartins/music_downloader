import yt_dlp


def baixar_mp3(url):
    ydl_opts = {
        "format": "ba/b",  # Triest to download the best audio format available
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": "%(title)s.%(ext)s",
        "nocheckcertificate": True,
        "prefer_ffmpeg": True,
        "logtostderr": False,
        "quiet": False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Starting download...")
            ydl.download([url])
            print("\nThe download is complete!")
    except Exception as e:
        print(f"An error was found: {e}")


if __name__ == "__main__":
    link = input("Enter the URL of the YouTube video you want to download as MP3: ")
    baixar_mp3(link)
