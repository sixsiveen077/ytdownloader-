def progress_hook(d):
    if d['status'] == 'downloading':

        percent = d.get('_percent_str', '0%').strip()
        speed = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()

        print(f"\r⬇ {percent} | ⚡ {speed} | ⏳ {eta}", end="")

    elif d['status'] == 'finished':
        print("\n\n✅ Download completed successfully!\n")
