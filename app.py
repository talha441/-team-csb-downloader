from flask import Flask, request, jsonify, send_file
from pytube import Playlist
import os
import zipfile
import uuid

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/download', methods=['GET'])
def download_playlist():
    playlist_url = request.args.get('url')

    if not playlist_url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        playlist = Playlist(playlist_url)
        unique_id = str(uuid.uuid4())
        folder_path = os.path.join(DOWNLOAD_FOLDER, unique_id)
        os.makedirs(folder_path)

        for video in playlist.videos:
            stream = video.streams.get_highest_resolution()
            stream.download(folder_path)

        zip_path = os.path.join(DOWNLOAD_FOLDER, f"{unique_id}.zip")
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=file)

        return send_file(zip_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
