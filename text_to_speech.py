from elevenlabs import generate, set_api_key
set_api_key("dd435b067e4a6b1fb642f4f9188705e5")

VOICE_MAPPING = {
    "female": "Rachel",
    "male": "Josh"
}


def text_to_speech(text, detected_gender):
    voice = VOICE_MAPPING.get(detected_gender, "Josh")  # Default to "Josh" if gender is not recognized
    audio = generate(
        text=text,
        voice=voice,
        model="eleven_multilingual_v2"
    )

    with open('new_audio.mp3', mode='bx') as f:
        f.write(audio)

    return audio
