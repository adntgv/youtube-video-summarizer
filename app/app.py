#!/usr/bin/python3
from flask import Flask, request, jsonify
import asyncio
import markdown

from summarizer import Summarizer
from transcriber import Transcriber

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello world!"

@app.route("/api", methods=["POST"])
def api():
    data = request.get_json()
    id = data['id'] if 'id' in data else None
    if not id:
        return jsonify({'error': 'Could not transcribe'})
    transcriber, summarizerInstance = initServices()
    transcription = asyncio.run(transcriber.youtube_transcribe(id))
    if transcription == "Error":
        return jsonify({'error': 'Could not transcribe'})
    summary = summarizerInstance.transcription_summarize(transcription, "html")
    htmlSummary = markdown.markdown(summary)
    return jsonify({'summary': htmlSummary})

def initServices():
    summarizerInstance = Summarizer()
    transcriber = Transcriber()
    return transcriber, summarizerInstance