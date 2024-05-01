from flask import Flask, request, jsonify
from libraries.deviceManager import AudioManager
from libraries.textToSpeech import TextToSpeech

app = Flask(__name__)

@app.route('/push-to-assistant/tts', methods=['POST'])
def text_to_speech():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    if 'message' not in data or 'endDevice' not in data:
        return jsonify({"error": "JSON must contain 'message' and 'endDevice' fields"}), 400
    
    try:
        audioManager = AudioManager(data["endDevice"])
        if (audioManager.isAudioDeviceBusy()):
            audioManager.stopManager()
            return jsonify({"status": False, "message": "End device is busy", "errorType": "END_DEVICE_BUSY"}), 200
        else:
            tts = TextToSpeech()
            audio = tts.convertTextToSpeech(data["message"])
            audioManager.playAudio(audio)
            audioManager.stopManager()
            return jsonify({"status": True, "message": "Success", "errorType": ""}), 200
    except NameError as e:
        return jsonify({"status": False, "message": str(e), "errorType": "END_DEVICE_ERROR"}), 200
    except ConnectionError as e:
        return jsonify({"status": False, "message": "Internet connection of server is down. Please try later", "errorType": "NO_INTERNET_IN_SERVER"}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An error occured {e}", "errorType": "UNKNOWN_ERROR"}), 200

if __name__ == '__main__':
    app.run(port=8082)