# AudioScribe: Flask-based Speech-to-Text Application

## Project Overview

**AudioScribe** is a **Flask-based web application** that allows users to upload audio files and get real-time transcriptions using the **AssemblyAI API**. The application supports both **file uploads** and **live speech-to-text transcription** via the **Web Speech API**.

### Features:
- **Upload Audio Files**: Upload MP3, WAV, or OGG files and get transcriptions.
- **Real-Time Transcription**: Convert live speech into text using the Web Speech API (via a microphone).
- **Integration with AssemblyAI**: Uses the AssemblyAI API to process and transcribe the uploaded audio.
- **Socket.IO for Real-Time Communication**: Uses **Flask-SocketIO** for sending transcription updates to the client in real-time.

## Tech Stack:
- **Backend**: Flask (Python web framework)
- **Real-Time Communication**: Flask-SocketIO
- **API Integration**: AssemblyAI API for transcription
- **Frontend**: HTML, CSS, JavaScript (for real-time updates and audio file uploads)
- **Web Speech API**: Used for real-time speech-to-text transcription
- **Deployment**: Vercel (for cloud hosting)

## Installation Guide

### 1. Clone the Repository
Start by cloning this repository to your local machine:
```bash
git clone https://github.com/Hasninemamud/AudioScribe.git
cd AudioScribe
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Add Your AssemblyAI API Key
```bash
API_KEY = 'your-assemblyai-api-key'
```
### 4. Run the Application
```bash
python app.py
```
