from rich.console import Console
from rich.panel import Panel

console = Console()

def show_menu():
    console.clear()

    console.print(Panel.fit(
        "🎬 YouTube Downloader Pro",
        style="bold cyan"
    ))

    console.print("\n📌 Select an option:\n")

    console.print("[1] 📹 Download Video")
    console.print("[2] 🎧 Download Audio")
    console.print("[3] 📂 Download Playlist")
    console.print("[5] 📜 View History")   # 👈 NEW OPTION
    console.print("[4] ❌ Exit\n")

    choice = input("👉 Enter choice: ")
    return choice
