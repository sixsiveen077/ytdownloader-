import yt_dlp

def download_audio(url, path, progress_hook):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{path}/audio/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'continuedl': True,
        'progress_hooks': [progress_hook]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

