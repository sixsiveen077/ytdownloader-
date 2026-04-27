import json

from utils.logger import view_history
from ui.menu import show_menu
from ui.progress import progress_hook

from utils.validator import is_valid_url
from utils.file_manager import ensure_dirs
from utils.logger import log

from downloader.video import download_video, get_available_formats
from downloader.audio import download_audio
from downloader.playlist import download_playlist

# Load config
with open("config.json") as f:
    config = json.load(f)

BASE_PATH = config["download_path"]

# Create folders
ensure_dirs()

print("\n==============================")
print("  YouTube Downloader CLI App")
print("==============================\n")


while True:
    choice = show_menu()

    # ================= VIDEO =================
    if choice == "1":
        url = input("Enter YouTube URL: ")

        if not is_valid_url(url):
            print("❌ Invalid URL")
            continue

        try:
            # Get available qualities
            formats = get_available_formats(url)

            if not formats:
                print("❌ No formats found")
                continue

            print("\n📺 Available Qualities:\n")

            for i, f in enumerate(formats):
                print(f"{i+1}. {f['resolution']} ({f['ext']})")

            q = int(input("\nSelect quality number: ")) - 1

            if q < 0 or q >= len(formats):
                print("❌ Invalid selection")
                continue

            selected_format = formats[q]["format_id"]

            download_video(url, BASE_PATH, selected_format, progress_hook)

            print("\n📁 Saved to:")
            print("👉 /storage/emulated/0/YouTubeDownloader/videos")

            log("Video downloaded successfully")

        except Exception as e:
            print("Error:", e)
            log(str(e))

    # ================= AUDIO =================
    elif choice == "2":
        url = input("Enter YouTube URL: ")

        if not is_valid_url(url):
            print("❌ Invalid URL")
            continue

        try:
            download_audio(url, BASE_PATH, progress_hook)
            log("Audio downloaded successfully")

        except Exception as e:
            print("Error:", e)
            log(str(e))

    # ================= PLAYLIST =================
    elif choice == "3":
        url = input("Enter Playlist URL: ")

        if not is_valid_url(url):
            print("❌ Invalid URL")
            continue

        try:
            download_playlist(url, BASE_PATH, progress_hook)
            log("Playlist downloaded successfully")

        except Exception as e:
            print("Error:", e)
            log(str(e))

    elif choice == "5":
        view_history()

    # ================= EXIT =================
    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option")
