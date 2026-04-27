from datetime import datetime

LOG_FILE = "logs.txt"

def log(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time}] {message}\n")
def view_history():
    import json
    import os

    if not os.path.exists("history.json"):
        print("\n📭 No history found.\n")
        return

    with open("history.json", "r") as f:
        logs = json.load(f)

    if not logs:
        print("\n📭 History is empty.\n")
        return

    print("\n📜 Download History:\n")

    for i, entry in enumerate(logs[-10:], 1):  # last 10 logs
        print(f"{i}. {entry['time']}")
        print(f"   ➤ {entry['message']}\n")
