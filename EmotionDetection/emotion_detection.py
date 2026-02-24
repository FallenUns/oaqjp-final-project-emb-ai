import json
import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze: str) -> dict:
    """
    Sends text to Watson NLP EmotionPredict endpoint and returns a formatted dictionary:
    {
        'anger': <float>,
        'disgust': <float>,
        'fear': <float>,
        'joy': <float>,
        'sadness': <float>,
        'dominant_emotion': <str>
    }
    """
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, headers=HEADERS, json=payload, timeout=30)

    response_dict = json.loads(response.text)

    emotions = response_dict["emotionPredictions"][0]["emotion"]
    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
    }

    dominant_emotion = max(scores, key=scores.get)

    scores["dominant_emotion"] = dominant_emotion
    return scores