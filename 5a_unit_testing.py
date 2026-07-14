import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_emotion_detector_joy(self):
        result = emotion_detector("I am very happy today!")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_detector_anger(self):
        result = emotion_detector("I am really angry about this!")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_emotion_detector_sadness(self):
        result = emotion_detector("I am feeling very sad today.")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_emotion_detector_disgust(self):
        result = emotion_detector("This food tastes disgusting!")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_emotion_detector_fear(self):
        result = emotion_detector("I am scared of the dark.")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
