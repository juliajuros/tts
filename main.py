from flask import Flask, jsonify, request
import pyttsx3

#from bitstring import BitArray

#def binary(name):
#    b=BitArray(bytes=open(name,'rb').read())
    #with open('binary.txt', 'w') as file1:
    #   file1.write(b.bin)
#    return b.bin

def opeen(file):
    with open(file, encoding ='unicode_escape') as f:
        data = f.read()
    return data
def tts(text, rate = 150, volume = 1):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    #engine.save_to_file(text, 'tekst.wav')
    engine.save_to_file(text, 'tekst.txt')
    engine.runAndWait()
    data = opeen("tekst.txt")
    #bin = binary('tekst.wav')
    return data

app = Flask(__name__)
@app.route('/')
def home():
    txt = 'stol z powylamywanymi nogami, chrzaszcz brzmi w trzcinie w szczebrzeszynie'
    return jsonify({"output-text": tts(txt)})
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
#  --data '{"text":"dżdżownica i jeż"}' \
#localhost:56733/json

#curl --header "Content-Type: application/json"   --request POST   --data '{"text":"dżdżownica i jeż"}' localhost:5000/json

#sudo docker rm -f
#sudo docker build -t tts .
#sudo docker run -p 5000:5000 --name TTS tts
