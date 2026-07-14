import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        response = requests.post(url, json=input_json, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            emotion_predictions = response_data.get('emotion_predictions', [])
            if emotion_predictions:
                emotion_data = emotion_predictions[0].get('emotion', {})
                
                anger = emotion_data.get('anger', 0)
                disgust = emotion_data.get('disgust', 0)
                fear = emotion_data.get('fear', 0)
                joy = emotion_data.get('joy', 0)
                sadness = emotion_data.get('sadness', 0)
                
                emotions = {
                    'anger': anger,
                    'disgust': disgust,
                    'fear': fear,
                    'joy': joy,
                    'sadness': sadness
                }
                dominant_emotion = max(emotions, key=emotions.get)
                
                return {
                    'anger': anger,
                    'disgust': disgust,
                    'fear': fear,
                    'joy': joy,
                    'sadness': sadness,
                    'dominant_emotion': dominant_emotion
                }
        
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    except Exception as e:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
