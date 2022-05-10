import speech_recognition
# import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:

    try:

        with speech_recognition.Microphone(0) as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            # text = recognizer.recognize_google(audio, key="AIzaSyA676wOTMtotsYPnwQzrciYxycCZ-IumeA")
            # text = recognizer.recognize_sphinx(audio)
            # text = recognizer.recognize_bing(audio, key="2f972d2f5199467a8772cbda305232eb")
            text = text.lower()

            print(f"Recognized {text}")

    except speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        continue