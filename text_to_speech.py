from elevenlabs import generate

def text_to_speech(text, detected_gender, is_video, video_path=None):
    if detected_gender == 'female':
        audio = generate(
            text=text,
            voice="Rachel",
            model="eleven_multilingual_v2"
        )
    else:
        audio = generate(
            text=text,
            voice="Josh",
            model="eleven_multilingual_v2"
        )

        # if is_video:

    with open('new_audio.mp3', mode='bx') as f:
        f.write(audio)

        # Download file
    files.download('new_audio.mp3')

    return audio