#!/usr/bin/env python
# coding: utf-8

# In[3]:


import speech_recognition as sr
import pyttsx3
import datetime

r = sr.Recognizer()    
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def takecom():
        
    try:
        with sr.Microphone() as source:
            print("Listening....")
            if trigger == True:
                talk("I am Listening")
            r.adjust_for_ambient_noise(source, duration=0.2) 
            if trigger == True:
                talk("Command Please")
            print("Command Please")
            audio = r.listen(source)
            print("Recognising.") 
            text = r.recognize_google(audio)
            print(text)
    except Exception:                
        print("Network connection error") 
        
        return "none"
    return text

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
trigger = False
    
while 1:
    if trigger == False:
        sw = takecom().lower()
        if 'assistant' in sw:
            trigger = True
            talk("Interactive mode activated")
            
        while trigger:
            sw = takecom().lower()
            if 'time' in sw:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
            elif 'lift' in sw:
                talk('Raising to 105 degrees')
            elif 'drop' in sw:
                talk('Lowering it to 180 degree')
            elif 'climb' and 'up' in sw:
                talk('Raising it by 15 degree')
            elif 'climb' and 'down' in sw:
                talk('Lowering it by 15 degree')
            elif 'exit' in sw:
                trigger = False
                talk('Listening mode activated')
            else:
                talk('Please say the command again.')


# In[ ]:





# In[ ]:





# In[ ]:




