from gtts import gTTS
import os
import speech_recognition as sr


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something")
        audio = r.listen(source)
        print("Thank you for your input.")

    mytext = r.recognize_google(audio, language="en-in")
    try:
        print("You said: ", mytext)

    except:
        mytext = "I did not understand what you said!"

    return mytext


def text_to_speech(mytext):
    myobj = gTTS(text=mytext, lang="en-in", slow=False)

    myobj.save("CSM104.mp3")
    os.system("CSM104.mp3")


text_to_speech(speech_to_text())
