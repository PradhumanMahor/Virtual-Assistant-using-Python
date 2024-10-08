import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your virtual assistant. Please tell me how may I help you")


def takeCommand():
#It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        # print(audio)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_details():
    url = "https://www.straive.com" #Our Company website
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    try:
        response = requests.get(url , headers = headers)
        soup = BeautifulSoup(response.content, 'html.parser')
       
        data_container = soup.find('div', class_='rich-text12')
        if data_container:
            company_paragraphs = company_div.find_all('p')[1:2]  
            summary = '\n'.join([p.get_text() for p in company_paragraphs])
            return summary
        else:
            print("Company information container not found.")
            return None
    except Exception as e:
        print(f"Error fetching company information")
        return None


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'search' in query:
            speak('Searching on Wikipedia wait for a moment Sir...')
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'our company' in query:
            talk('Sure Sir')
            summary = get_details()
            if summary:
                print(summary)
                talk(summary)
            else:
                talk('Error finding the details, Sorry for the inconvinence sir !!')



        #command to open the youtube on the browser
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
            
        # play command used for play song on youtube
        elif 'play' in query:
            song = query.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        
        # when some entry recorded for the greetings
        elif 'thank you' in query:
            talk('your welcome')
            talk('Is their anything more that i can help you sir')
            leaveCommand = takeCommand().lower()
            if 'yes' in leaveCommand:
                talk('Please Wait')
                continue
            elif 'no' in leaveCommand:
                talk('Thank you Sir')
                break
        
        #name for the team members
        elif 'team members' in query:
            talk('The Team Members in this project are Pradhuman and Shreyansh')
        
        #open google in the browser
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        # opening the manit website
        elif 'open nit bhopal' in query:
            webbrowser.open("manit.ac.in")
        
        # opening the python project in the directory 
        # elif 'python project' in query:
        #     codePath = "D:\6th Semester\ai\llabs\AI_project.py"
        #     os.startfile(codePath)
        
        #mentioning the the current time 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'stop' in query:
            break