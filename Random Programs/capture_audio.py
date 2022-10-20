import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as mic:
    r.adjust_for_ambient_noise(mic, duration=.02)
    audio = r.listen(mic)

    text = r.recognize_google(audio)
    text = text.lower()

    print(f"Recognized: {text}")

    with open('speech.wav', 'wb') as f:
        f.write(audio.get_wav_data())
