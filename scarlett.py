
# Libraries used in the project

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import requests
import webbrowser
import sys
import bs4
import pyjokes
import wikipedia as googleScrap
import cv2




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source :

            print('Listening to you .....')  

            voice = listener.listen(source)
            
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'scarlet' in command:
                command = command.replace('scarlet','')
                print(command)

    except:
        pass
    return command







def runscarlet():
    command = take_command()
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing .. .. '+ song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is  '+ time)

    elif 'joke' in command:
        talk(pyjokes.get_joke())


    
   
    elif 'google' in command:
        command = command.replace('google','')
        talk("This is what I found on google about " )
        talk(command)

        try:
            pywhatkit.search(command)
            result = googleScrap.summary(command,2)
            talk(result)

        except:
            talk("NO speakable Data Available")


   

    elif 'exit' in command:
        talk("Scarlet signing off")
        return False

    
    

#Driver Code
talk ('I am scarlett')
talk('how can i help you today')   

runscarlet()
