import requests
import uuid
import json
from flask import Flask, request, render_template, send_file, jsonify
from AI_Chatbot_Implementation import AIChatBot
from ToTalk import Text_to_Audio

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/textToSpeech", methods=["POST"])
def text_to_speech():
    user_input = request.form.get("messages")
    user_input = json.loads(user_input)
    newChat = AIChatBot()
    response = newChat.get_ai_response_from_full_conversation_history(user_input)
    return jsonify({"messages": response})

@app.route("/getAudio", methods=["POST"])
def getaudio():
    user_message = request.form.get("message")
    audio_file = Text_to_Audio(user_message)
    return send_file(audio_file, as_attachment=True)

#if __name__ == "__main__":
    #app.run(debug=True)