import os

from flask import Flask, jsonify, request
import pyttsx3
# nano main.py
# python3 main.py

def tts(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.save_to_file(text, 'tekst.mp3')
    engine.runAndWait()
    # fopen
    # json
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
    app.run(host='0.0.0.0', port = os.getenv("PORT"))
#curl in terminal: curl http://192.168.0.81:50000

#curl --header "Content-Type: application/json" \
#  --request POST \
#  --data '{"text":"dżdżownica i jeż"}' \
#localhost:56733/json
