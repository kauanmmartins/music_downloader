import yt_dlp


def baixar_mp3(urls):
    ydl_opts = {
        "format": "ba/b",  # Tries to download the best audio format available
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
            ydl.download(urls)
            print("\nThe download is complete!")
    except Exception as e:
        print(f"An error was found: {e}")


if __name__ == "__main__":
    links_input = input("Enter the URLs of the YouTube videos you want to download as MP3, separated by commas: ")
    links = [link.strip() for link in links_input.split(',')]
    baixar_mp3(links)
