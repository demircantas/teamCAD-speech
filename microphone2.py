import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone(0) as source:
    print("Say anything : ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text['transcription']))
    except:
        print("sorry, no go!")