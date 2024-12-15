# 1a0d497a5fa440e4b21b320a7bd11172


import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your AssemblyAI API key
API_KEY = '1a0d497a5fa440e4b21b320a7bd11172'
API_UPLOAD_URL = "https://api.assemblyai.com/v2/upload"
TRANSCRIPT_API_URL = "https://api.assemblyai.com/v2/transcript"

# Set headers with your API Key
HEADERS = {
    'authorization': API_KEY
}

@app.route('/')
def index():
    return render_template('index.html')

# Route for uploading the audio file
@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # Upload the audio file to AssemblyAI
    response = requests.post(API_UPLOAD_URL, headers=HEADERS, files={'file': file})
    if response.status_code == 200:
        audio_url = response.json()['upload_url']
        # Start transcription once the audio file is uploaded
        return jsonify({'audio_url': audio_url})
    else:
        return jsonify({'error': 'Failed to upload file'}), 500

# Route for transcribing the uploaded audio file
@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    audio_url = request.json.get('audio_url')
    if not audio_url:
        return jsonify({'error': 'No audio URL provided'}), 400

    # Request transcription from AssemblyAI
    response = requests.post(
        TRANSCRIPT_API_URL,
        headers=HEADERS,
        json={'audio_url': audio_url}
    )
    if response.status_code == 200:
        transcript_id = response.json()['id']
        return jsonify({'message': 'Transcription started', 'transcript_id': transcript_id})
    else:
        return jsonify({'error': 'Failed to start transcription'}), 500

# Route to get the transcript once it's ready
@app.route('/get-transcript', methods=['GET'])
def get_transcript():
    transcript_id = request.args.get('transcript_id')
    if not transcript_id:
        return jsonify({'error': 'No transcript ID provided'}), 400

    # Check the status of the transcription
    response = requests.get(
        f"{TRANSCRIPT_API_URL}/{transcript_id}",
        headers=HEADERS
    )
    if response.status_code == 200:
        transcript_data = response.json()
        if transcript_data['status'] == 'completed':
            return jsonify({'transcript': transcript_data['text']})
        else:
            return jsonify({'status': transcript_data['status']}), 202
    else:
        return jsonify({'error': 'Failed to get transcript'}), 500

if __name__ == '__main__':
    app.run(debug=True)