import re

def is_valid_url(url):
    if not url:
        return False

    pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+"
    return re.match(pattern, url) is not None

def clean_filename(name):
    return "".join(c for c in name if c not in r'\/:*?"<>|')
