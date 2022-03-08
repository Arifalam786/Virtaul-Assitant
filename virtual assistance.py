#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


# In[10]:


engine = pyttsx3.init('sapi5')


# In[11]:


voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)


# In[ ]:



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("good morning")
    elif hour>= 12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am your virtual assistant. sir, Please tell me how may i help you")
def takeCommand():
    #it takes microphone as input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f'user said: {query}\n')
       
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    #speak("arif is a good boy")
    wishMe()
  
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('searching on youtube')
            query = query.replace('open youtube',"")
            speak('according to youtube')
            webbrowser.open(f'youtube.com/{query}')
            
        #elif 'open youtube' in query:
            #webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('according to google')
            query = query.replace('open google',"")
            speak('according to google.')
            webbrowser.open(f'google.com/{query}')
        elif 'play music' in query:
            music_dir = 'C:\\new music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir, the time is {strTime}')
        
        elif 'exit' in query:
            break
        
            
          
        
         
            
            
        
    
      


# In[20]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




