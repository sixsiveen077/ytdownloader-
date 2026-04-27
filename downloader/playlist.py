import yt_dlp

def download_playlist(url, path, progress_hook):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{path}/playlists/%(playlist)s/%(title)s.%(ext)s',
        'noplaylist': False,
        'continuedl': True,
        'progress_hooks': [progress_hook]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
