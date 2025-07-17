from flask import Flask, request, render_template
from pytube import Playlist
import yt_dlp
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download')
def download():
    url = request.args.get("url")

    if "youtube.com/playlist" in url:
        return handle_youtube_playlist(url)
    elif "facebook.com" in url:
        return handle_facebook_playlist(url)
    elif "drive.google.com" in url:
        return handle_gdrive_file(url)
    elif "terabox" in url:
        return handle_terabox_file(url)
    else:
        return "Unsupported URL"

def handle_youtube_playlist(url):
    playlist = Playlist(url)
    video_links = [video.watch_url for video in playlist.videos]
    return render_template("result.html", links=video_links, title="YouTube Playlist")

def handle_facebook_playlist(url):
    ydl_opts = {'quiet': True, 'extract_flat': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)
        entries = result.get("entries", [])
        video_links = [entry['url'] for entry in entries]
    return render_template("result.html", links=video_links, title="Facebook Playlist")

def handle_gdrive_file(url):
    file_id_match = re.search(r"/d/([a-zA-Z0-9_-]+)", url)
    if file_id_match:
        file_id = file_id_match.group(1)
        direct_link = f"https://drive.google.com/uc?export=download&id={file_id}"
        return render_template("result.html", links=[direct_link], title="Google Drive File")
    return "Invalid Google Drive URL"

def handle_terabox_file(url):
    # Placeholder: real script/API integration needed
    return render_template("result.html", links=["Terabox download link coming soon"], title="Terabox File")

if __name__ == '__main__':
    app.run(debug=True)
