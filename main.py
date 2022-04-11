# Projet "Youtube Downloader"
# module : pytube

from pytube import Playlist, Channel, YouTube

url = "https://www.youtube.com/watch?v=RgzX4qrLmPM&list=PLXDBYzqsqO3WWt09nLBmynZlL6n8-7bQV"


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize

    print(f"Progression du téléchargement {int(percent)}%")


p = Playlist(url)
for url in p.video_urls:
    try:
        video = YouTube(url)
    except:
        print(f'Video {url} is unavaialable, skipping.')
    else:
        video.register_on_progress_callback(on_download_progress)
        stream = video.streams.get_highest_resolution()
        print("Téléchargement...")
        stream.download()
        print("OK")
