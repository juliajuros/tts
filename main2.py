from flask import Flask, request, jsonify
import pyttsx3
import re

def tts(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.save_to_file(text, 'tekst.wav')
    engine.runAndWait()
    return text

app = Flask(__name__)
@app.route('/post', methods=['POST'])
def post_route():
    if request.method == 'POST':
        data = request.get_json(force=True)
        txt = data['text']
        out = []
        for t in txt:
            temp = tts(t)
            temp = re.sub(r'[^\w]', ' ', temp)
            out.append(temp)
        print('Data Received: "{data}"'.format(data=data))
        return jsonify({"output-text": out})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

    #curl 192.168.0.81:5000/post -d '{"text": ["Andrzej","traktor"]}' -H 'Content-Type:application/json'
