from elevenlabs import generate

VOICE_MAPPING = {
    "female": "Rachel",
    "male": "Josh"
}

def text_to_speech(text, detected_gender, is_video, video_path=None):
    voice = VOICE_MAPPING.get(detected_gender, "Josh")  # Default to "Josh" if gender is not recognized
    audio = generate(
        text=text,
        voice=voice,
        model="eleven_multilingual_v2"
    )

    # if is_video:

    with open('new_audio.mp3', mode='bx') as f:
        f.write(audio)

        # Download file
    files.download('new_audio.mp3')

    return audio