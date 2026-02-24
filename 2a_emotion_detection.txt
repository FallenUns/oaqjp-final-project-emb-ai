import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze: str) -> str:
    """
    Sends text to Watson NLP EmotionPredict endpoint and returns the response text.
    """
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(URL, headers=HEADERS, json=payload, timeout=30)

    # The lab instruction wants the *text attribute* of the response object
    return response.text