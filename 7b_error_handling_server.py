from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    try:
        data = request.get_json()
        
        # Check if text is provided or blank
        if data is None or 'text' not in data or data['text'].strip() == '':
            return jsonify({"error": "Invalid text! Please try again."}), 400
        
        text = data['text']
        result = emotion_detector(text)
        
        if result['dominant_emotion'] is None:
            return jsonify({"error": "Invalid text! Please try again."}), 400
        
        response = {
            "anger": result['anger'],
            "disgust": result['disgust'],
            "fear": result['fear'],
            "joy": result['joy'],
            "sadness": result['sadness'],
            "dominant_emotion": result['dominant_emotion']
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return "Emotion Detection API is running! Use POST /emotionDetector"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
