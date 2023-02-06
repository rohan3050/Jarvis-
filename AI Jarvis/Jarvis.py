from Brain.AiBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting the jarvis : Wait for some second")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting The Jarvis : wait for few second")
#from Main import MainTaskExecution
def MainExecution():
    Speak("Hello sir")
    Speak("I'm jarvis, I'm ready to assist you")
    
    while True:
        
        Data = MicExecution()
        Data = str(Data)
        #ValueReturn = MainTaskExecution(Data)
        #if ValueReturn==True:
        #   pass
        
        if len(Data)<1:
            pass
        
        elif "turn on the tv" in Data: #specific command
            Speak("ok... Turning on the Android TV")
        
        elif "what is " in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)
    
    
def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> wakeup Detected!! >>")
        print("")
        MainExecution()   
        
    else:
        pass
    
    
    
ClapDetect()
