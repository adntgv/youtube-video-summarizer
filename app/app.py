#!/usr/bin/python3
from flask import Flask, request, jsonify
import asyncio
import markdown

from summarizer import Summarizer
from transcriber import Transcriber
from bot import Bot

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello world!"

@app.route("/api/summarize", methods=["POST", "OPTIONS"])
def api():
    if request.method == "OPTIONS":
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)
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
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600'
    }
    
    return jsonify({'summary': htmlSummary}), 200, headers

@app.route("/bot/telegram", methods=["POST"])
def bot_telegram():
    data = request.get_json()
    bot = Bot()
    asyncio.run(bot.bot_tele(data))
    return jsonify({'status': 'ok'})

def initServices():
    summarizerInstance = Summarizer()
    transcriber = Transcriber()
    return transcriber, summarizerInstance