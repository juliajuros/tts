import os
from flask import Flask, jsonify, request
import pyttsx3

def tts(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.save_to_file(text, 'tekst.mp3')
    engine.runAndWait()
    return text

app = Flask(__name__)
@app.route('/')
def home():
    txt = 'stół z powyłamywanymi nogami, chrząszcz brzmi w trzcinie w szczebrzeszynie'
    return jsonify({"output-text": tts(txt)})
@app.route('/json', methods=['POST'])
def json_example():
    req_data = request.get_json()
    txt = req_data['text']
    #alphabet = req_data['alphabet'] -nasze?
    output = tts(txt)
    return jsonify({"output-text": output})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)

#curl --header "Content-Type: application/json"   --request POST   --data '{"text":"dżdżownica i jeż"}' localhost:5000/json

#sudo docker rm -f
#sudo docker build -t tts .
#sudo docker run -p 5000:5000 --name TTS tts
