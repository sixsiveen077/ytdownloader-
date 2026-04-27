import yt_dlp

# =========================
# GET AVAILABLE FORMATS
# =========================
def get_available_formats(url):
    ydl_opts = {'quiet': True}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    formats = []

    for f in info.get('formats', []):
        if f.get('height'):
            formats.append({
                "format_id": f["format_id"],
                "resolution": f"{f.get('height')}p",
                "ext": f.get("ext")
            })

    # remove duplicate resolutions
    unique = {}
    for f in formats:
        unique[f["resolution"]] = f

    return list(unique.values())


# =========================
# FAST DOWNLOAD VIDEO
# =========================
def download_video(url, path, format_id, progress_hook):

    ydl_opts = {
        # 🎯 best video + audio
        'format': 'bv*+ba/best',

        # 📁 save path
        'outtmpl': f'{path}/videos/%(title)s.%(ext)s',

        # 🔊 merge output
        'merge_output_format': 'mp4',

        # 📊 progress
        'progress_hooks': [progress_hook],

        'noplaylist': True,

        # 🚀 SPEED BOOST SETTINGS
        'concurrent_fragment_downloads': 5,
        'buffersize': 1024 * 1024 * 16,   # 16MB
        'http_chunk_size': 10485760,      # 10MB

        # 🔁 RESUME + STABILITY
        'continuedl': True,
        'nopart': False,
        'retries': 10,
        'fragment_retries': 10,

        # ⏱️ network
        'socket_timeout': 30,

        # 🔧 ffmpeg merge
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
