#!/data/data/com.termux/files/usr/bin/bash

echo "🔄 Updating packages..."
pkg update -y && pkg upgrade -y

echo "📦 Installing dependencies..."
pkg install python ffmpeg git -y

echo "🐍 Installing Python libraries..."
pip install yt-dlp rich requests

echo "📁 Setting up folders..."
mkdir -p ~/ytdownloader/downloads/videos
mkdir -p ~/ytdownloader/downloads/audio
mkdir -p ~/ytdownloader/downloads/playlists

echo "🔐 Giving permissions..."
chmod -R 755 ~/ytdownloader

echo "📂 Moving to project..."
cd ~/ytdownloader

echo "🚀 Starting YouTube Downloader..."
python main.py
