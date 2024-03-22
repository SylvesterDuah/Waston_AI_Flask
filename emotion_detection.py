import requests

def emotion_detector(text_to_analyze):

    if not text_to_analyze.strip():
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=data, headers=headers)
    if response.ok:
        response_data = response.json()
       
        emotions = response_data.get('emotions', {})

        dominant_emotion = max(emotions, key=emotions.get) if emotions else None

        output = {
            'anger': emotions.get('anger'),
            'disgust': emotions.get('disgust'),
            'fear': emotions.get('fear'),
            'joy': emotions.get('joy'),
            'sadness': emotions.get('sadness'),
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:

        output = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:

        output = "Error in emotion detection"

    return output
