from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
import ast

app = Flask(__name__)

# Static code analysis function
def analyze_code(code_snippet):
    try:
        tree = ast.parse(code_snippet)
        # Basic analysis: count lines, functions, classes
        lines = len(code_snippet.split('\n'))
        functions = sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
        classes = sum(1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef))
        
        return {
            'lines': lines,
            'functions': functions,
            'classes': classes,
            'is_valid': True,
            'error': None
        }
    except SyntaxError as e:
        return {
            'lines': 0,
            'functions': 0,
            'classes': 0,
            'is_valid': False,
            'error': str(e)
        }

@app.route('/analyze', methods=['POST'])
def analyze_route():
    try:
        data = request.get_json()
        code_snippet = data.get('code', '')
        
        if not code_snippet.strip():
            return jsonify({"error": "No code provided"}), 400
        
        result = analyze_code(code_snippet)
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    try:
        data = request.get_json()
        
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
    return "Emotion Detection API is running! Use POST /emotionDetector or /analyze"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
