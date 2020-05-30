import pyttsx3 #text-to-speech package

#text-to-speech engine started
engine = pyttsx3.init()

# getting details of current speaking rate
rate = engine.getProperty('rate')
print(rate)
# set details of current speaking rate (speech speed)
engine.setProperty('rate', 200)

#to get all voice types (Male Or Female)
voices = engine.getProperty('voices')
#voices[0] - for Male Voice
#voices[1] - for Female Voice
engine.setProperty('voice', voices[0].id)
engine.say("Good Morning sir")
engine.runAndWait()