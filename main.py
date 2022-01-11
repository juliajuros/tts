from flask import Flask, jsonify, request
import os
from flask_cors import CORS
import base64
import logging

def binary(name):
    with open(name, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string.decode('ascii')
  
def tts(text, rate = 175, volume = 100):
    command = f"espeak -v pl -a {volume} -s {rate} \'{text}\' --stdout > tekst.wav"
    os.system(command)
    bin = binary('tekst.wav')
    return bin

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    txt = 'stol z powylamywanymi nogami, chrzaszcz brzmi w trzcinie w szczebrzeszynie'
    output = tts(txt)
    return jsonify({"output-text": output})


@app.route('/json', methods=['POST'])

def json_example():
    req_data = request.get_json()
    txt = req_data['text']
    volume = req_data['volume']
    rate = req_data['rate']
    out = []
    for t in txt:
        temp = tts(t)
        out.append(temp)
    app.logger.info('Data Received: "{data}"'.format(data=req_data))
    return jsonify({"output-text": out})

    volume = req_data['volume']
    rate = req_data['rate']
    output = tts(txt)
    return jsonify({"output-text": output})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
