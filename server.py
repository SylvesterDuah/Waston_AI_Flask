"""Flask server for emotion detection application."""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """The index.html template."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Detect emotion from the provided text.
    
    This endpoint expects a JSON payload with a 'text' key and returns
    the emotion analysis results.
    """
    content = request.json
    if not content or 'text' not in content or not content['text'].strip():
        return jsonify({"message": "Invalid text! Please try again!"})

    statement = content['text']
    emotion_response = emotion_detector(statement)
    
    if emotion_response['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"})
    
    response_text = "'anger': {:.9f}, 'disgust': {:.9f}, 'fear': {:.9f}, 'joy': {:.9f}, and 'sadness': {:.9f}. The dominant emotion is {}.".format(
        emotion_response.get('anger', 0),
        emotion_response.get('disgust', 0),
        emotion_response.get('fear', 0),
        emotion_response.get('joy', 0),
        emotion_response.get('sadness', 0),
        emotion_response.get('dominant_emotion', 'N/A')
    )

    return jsonify({"message": response_text})

if __name__ == '__main__':
    app.run(debug=True)
