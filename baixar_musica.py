import yt_dlp


def baixar_mp3(url):
    ydl_opts = {
        "format": "ba/b",  # Tenta baixar o melhor áudio disponível
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
            print("Iniciando download...")
            ydl.download([url])
            print("\nDownload concluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    link = input("Cole o link do vídeo do YouTube: ")
    baixar_mp3(link)
