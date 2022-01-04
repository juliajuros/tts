from flask import Flask, jsonify, request
from scipy.io import wavfile
import numpy as np
import os
from flask_cors import CORS
from bitstring import BitArray

app = Flask(__name__)
CORS(app)
def binary(name):
    b=BitArray(bytes=open(name,'rb').read())
    with open('binary.txt', 'w') as file1:
       file1.write(b.bin)
    return b.bin
def tts(text, rate = 50, volume = 100):
    command = f"espeak -a {volume} -s {rate} \'{text}\' --stdout > tekst.wav"
    os.system(command)
    bin = binary('tekst.wav')
    return bin

app = Flask(__name__)
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
    output = tts(txt, rate, volume)
    return jsonify({"output-text": output})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)

#curl --header "Content-Type: application/json" \
#  --request POST \
#  --data '{"text":"dżdżownica i jeż", "volume": 100, "rate": 50}' \
#localhost:56733/json

#curl --header "Content-Type: application/json"   --request POST   --data '{"text":"dżdżownica i jeż"}' localhost:5000/json

#sudo docker rm -f
#sudo docker build -t tts .
#sudo docker run -p 5000:5000 --name TTS tts
