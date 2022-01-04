from flask import Flask, jsonify, request
import os
from flask_cors import CORS
import base64

def binary(name):
    with open(name, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string.decode('ascii')
  
def tts(text, rate = 50, volume = 100):
    text = ' '.join(text)
    command = f"espeak -v pl -a {volume} -s {rate} \'{text}\' --stdout > tekst.wav"
    os.system(command)
    bin = binary('tekst.wav')
    return bin

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    txt = 'stol z powylamywanymi nogami, chrzaszcz brzmi w trzcinie w szczebrzeszynie'
    output = tts(txt)
    return jsonify({"output-text": output})


@app.route('/json', methods=['POST'])
def json_example():
    req_data = request.get_json()
    txt = req_data['text']
    print(txt)
    # volume = req_data['volume']
    # rate = req_data['rate']
    output = tts(txt)
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
