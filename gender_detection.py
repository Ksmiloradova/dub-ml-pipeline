import requests

API_URL = "https://api-inference.huggingface.co/models/alefiury/wav2vec2-large-xlsr-53-gender-recognition-librispeech"
headers = {"Authorization": f"Bearer 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"}

# Takes the filename of the audio with the voice
# Returns the voice gender ('female' or 'male'), str type

def voice_gender_detection(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()[0]['label']
