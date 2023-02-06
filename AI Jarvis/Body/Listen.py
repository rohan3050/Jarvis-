#hindi or english - command
#english

#step - 1
#pip install googletrans==3.1.0a0

#step -2
#three function
# 1 Listen function
# 2 english translation
# 3 connect

import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0

# 1 Listen function
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #listening Mode....

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""

    query = str(query).lower()
    return query
    
    

# translation
def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}.")
    return data


# 3 - connect
def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

