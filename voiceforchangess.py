import datetime
import os
import random
import string
import webbrowser
import pandas as pd
import pyttsx3
import speech_recognition as sr
import googlemaps
from twilio.rest import Client


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    print(text)
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except Exception as e:
            print(f"Error: {e}")
            say("I beg your pardon, Please repeat")
            return None

def take_name():
    while True:
        say("Activation mode on!If you are in trouble say safeguard!")
        nam = takecommand()
        return nam
contacts_messages = {
    "+91 8826284815": "I am in trouble please help",
    "91 9990193405": "Urgent: I need assistance",
}
gmaps = googlemaps.Client(key='AIzaSyD8L7GuWwJBe3Kw7wXfkwHJH5qjyIfSZdc')

def get_current_location():
    try:
        location = gmaps.geolocate()

        
        latitude = location['location']['lat']
        longitude = location['location']['lng']

        return latitude, longitude
    except Exception as e:
        print("Error retrieving current location:", e)
        return None, None
    
def send_whatsapp_message(contact, message):

    account_sid = 'AC7f362944e534f07390eee3527036ca76'
    auth_token = 'c9912387b532cebdfde2d5b4a2f47d43'
    twilio_number = '+12185262645'


    client = Client(account_sid, auth_token)


    try:
        message = client.messages.create(
            body=message,
            from_='whatsapp:' + twilio_number,
            to='whatsapp:' + contact
        )
        print(f"WhatsApp message sent to {contact}: {message.sid}")
    except Exception as e:
        print(f"Error sending WhatsApp message to {contact}: {e}")




def send_whatsapp_message_with_location(contact, message):
    
    latitude, longitude = get_current_location()
    message_with_location = f"{message}\nLocation: https://www.google.com/maps?q={latitude},{longitude}"
    send_whatsapp_message(contact, message_with_location)

def send_message():
    for contact, message in contacts_messages.items():
      send_whatsapp_message_with_location(contact, message)
       


def redirect_to_google(query):
    google_search_url = "https://www.google.com/search?q="
    query = query.replace(" ", "+")
    search_url = f"{google_search_url}{query}"
    webbrowser.open(search_url)
    say(f"Here's what I found on web")

def thanos():
    say("I am your personal python assistant VoiceForChange")
    nam = take_name()

    while True:
        print("Listening.....")
        query = takecommand()
        sites = [["piracy", "https://fmoviesz.to/"],
                 ["youtube", "https://www.youtube.com/"],
                 ["wikipedia", "https://www.wikipedia.org/"],
                 ["whatsapp", "https://web.whatsapp.com/"],
                 ["instagram", "https://www.instagram.com/"],
                 ["python tutor", "https://pythontutor.com/render.html#mode=edit"],
                 ["google","https://www.google.co.in/"],
                 ["Facebook", "https://www.facebook.com/"],
                 ["Twitter", "https://twitter.com/"],
                 ["Instagram", "https://www.instagram.com/"],
                 ["LinkedIn", "https://www.linkedin.com/"],
                 ["Reddit", "https://www.reddit.com/"],
                 ["Pinterest", "https://www.pinterest.com/"],
                 ["Tumblr", "https://www.tumblr.com/"],
                 ["Snapchat", "https://www.snapchat.com/"],
                 ["WhatsApp", "https://web.whatsapp.com/"],
                 ["Skype", "https://web.skype.com/"],
                 ["Zoom", "https://zoom.us/"],
                 ["Netflix", "https://www.netflix.com/"],
                 ["Amazon", "https://www.amazon.com/"],
                 ["Ebay", "https://www.ebay.com/"],
                 ["Etsy", "https://www.etsy.com/"],
                 ["Wikipedia", "https://www.wikipedia.org/"],
                 ["Dictionary", "https://www.dictionary.com/"],
                 ["Thesaurus", "https://www.thesaurus.com/"],
                 ["Merriam-Webster", "https://www.merriam-webster.com/"],
                 ["GitHub", "https://github.com/"],
                 ["Stack Overflow", "https://stackoverflow.com/"],
                 ["Medium", "https://medium.com/"],
                 ["Quora", "https://www.quora.com/"],
                 ["BBC News", "https://www.bbc.com/news"],
                 ["CNN", "https://www.cnn.com/"],
                 ["The New York Times", "https://www.nytimes.com/"],
                 ["Weather", "https://www.weather.com/"],
                 ["Al Jazeera", "https://www.aljazeera.com/"],
                 ["National Geographic", "https://www.nationalgeographic.com/"],
                 ["TED", "https://www.ted.com/"],
                 ["Khan Academy", "https://www.khanacademy.org/"],
                 ["Coursera", "https://www.coursera.org/"],
                 ["Udemy", "https://www.udemy.com/"],
                 ["Duolingo", "https://www.duolingo.com/"],
                 ["Goodreads", "https://www.goodreads.com/"],
                 ["IMDb", "https://www.imdb.com/"],
                 ["Rotten Tomatoes", "https://www.rottentomatoes.com/"],
                 ["Spotify", "https://www.spotify.com/"],
                 ["SoundCloud", "https://soundcloud.com/"],
                 ["Pandora", "https://www.pandora.com/"],
                 ["Last.fm", "https://www.last.fm/"],
                 ["Genius (Lyrics)", "https://genius.com/"],
                 ["Unsplash", "https://unsplash.com/"],
                 ["Adobe Stock", "https://stock.adobe.com/"],
                 ["Canva", "https://www.canva.com/"],
                 ["Trello", "https://trello.com/"],
                 ["Asana", "https://asana.com/"],
                 ["Slack", "https://slack.com/"],
                 ["Dropbox", "https://www.dropbox.com/"],
                 ["Google Drive", "https://drive.google.com/"],
                 ["Microsoft Office 365", "https://www.office.com/"],
                 ["Grammarly", "https://www.grammarly.com/"],
                 ["Google Translate", "https://translate.google.com/"],
                 ["Vocabulary.com", "https://www.vocabulary.com/"],
                 ["Calm", "https://www.calm.com/"],
                 ["Headspace", "https://www.headspace.com/"],
                 ["Product Hunt", "https://www.producthunt.com/"],
                 ["Hacker News", "https://news.ycombinator.com/"],
                 ["Lichess (Chess)", "https://lichess.org/"],
                 ["Chess.com", "https://www.chess.com/"],
                 ["Codecademy", "https://www.codecademy.com/"],
                 ["LeetCode", "https://leetcode.com/"],
                 ["HackerRank", "https://www.hackerrank.com/"],
                 ["Repl.it", "https://replit.com/"],
                 ["Wolfram Alpha", "https://www.wolframalpha.com/"],
                 ["IFTTT", "https://ifttt.com/"],
                 ["Pinterest", "https://www.pinterest.com/"],
                 ["Zillow", "https://www.zillow.com/"],
                 ["Trulia", "https://www.trulia.com/"],
                 ["LinkedIn Learning", "https://www.linkedin.com/learning/"],
                 ["Vimeo", "https://vimeo.com/"],
                 ["Kahoot!", "https://kahoot.com/"],
                 ["Quizlet", "https://quizlet.com/"],
                 ["DuckDuckGo", "https://duckduckgo.com/"],
                 ["Bing", "https://www.bing.com/"],
                 ["Ecosia (Eco-Friendly Search)", "https://www.ecosia.org/"],
                 ["W3Schools", "https://www.w3schools.com/"],
                 ["Mozilla Developer Network (MDN)", "https://developer.mozilla.org/"],
                 ["MDN Web Docs", "https://developer.mozilla.org/"],
                 ["Stack Exchange", "https://stackexchange.com/"],
                 ["Jupyter Notebooks", "https://jupyter.org/"],
                 ["Anaconda", "https://www.anaconda.com/"],
                 ["Python.org", "https://www.python.org/"],
                 ["Real Python", "https://realpython.com/"],
                 ["Python Tutorial", "https://docs.python.org/3/tutorial/"],
                 ["Kaggle", "https://www.kaggle.com/"],
                 ["Towards Data Science", "https://towardsdatascience.com/"],
                 ["Tableau Public", "https://public.tableau.com/en-us/s/gallery"],
                 ["Google Trends", "https://trends.google.com/trends/trendingsearches/daily?geo=US"],
                 ["OpenWeatherMap", "https://openweathermap.org/"],
                 ["Nasa", "https://www.nasa.gov/"]
                  ]
        apps = [["chrome", r"C:\Program Files\Google\Chrome\Application\chrome.exe"],
                    ["edge", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"],
                    ["code", r"C:\Users\RAHUL\AppData\Local\Programs\Microsoft VS Code\Code.exe"],
                    ["camera",
                     r"C:\Program Files\WindowsApps\Microsoft.WindowsCamera_2023.2311.5.0_x64__8wekyb3d8bbwe\WindowsCamera.exe"],
                    ["pycharm", "C:\Program Files\JetBrains\PyCharm 2023.3.1\bin\pycharm64.exe"],
                    ["cpp", "C:\Program Files\JetBrains\CLion 2023.3.1\bin\clion64.exe"],
                    ["terminal", "C:\WINDOWS\system32\cmd.exe"]
                    ]

        letters = list(string.ascii_lowercase)
        should_continue = True
        if "safeguard".lower() in query.lower():
            say("Don't worry! We have activated trigger mode. Sending location to all emergency contacts...")
            location = get_current_location() 
            send_message()
            break 
       
        # if "Tell me a joke".lower() in query.lower() or "Chutkula sunao".lower() in query.lower():
        #     say("I will show you the biggest joke nearby")
        #     camera = r"C:\Program Files\WindowsApps\Microsoft.WindowsCamera_2023.2311.5.0_x64__8wekyb3d8bbwe\WindowsCamera.exe"
        #     os.startfile(camera)
        #     should_continue = False
        # elif "wire industry".lower() in query.lower() or "cable industry".lower() in query.lower() or "wire and cable industry".lower() in query:
        #     say("Sure sir, here are the details on google")
        #     webbrowser.open("https://www.google.com/search?q=all+about+wire+and+cable+industry&rlz=1C1RXQR_en-GBIN1069IN1069&oq=all+about+wire+and+cable+industry+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigATIHCAUQIRigATIKCAYQIRgWGB0YHjIKCAcQIRgWGB0YHjIKCAgQIRgWGB0YHjIKCAkQIRgWGB0YHtIBCTEyODA2ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
        #     should_continue = False
      
        for site in sites:
                if f"open {site[0]}".lower() in query or f"{site[0]} kholo".lower() in query:
                    say(f"Opening {site[0]} Site sir")
                    webbrowser.open(site[1])
                    should_continue = False
                    break

        for app in apps:
                if f"open {app[0]}".lower() in query or f"{app[0]} kholo".lower() in query:
                    say(f"Opening {app[0]} app sir")
                    os.startfile(app[1])
                    should_continue = False
                    break

        if not should_continue:
            break
        else:
            # say("Sorry ,the command is not available in my database.")
            # say("Please connect to my creator on linkdin and text him your command, to help him.")
            # say("He'll be grateful.")
            # say('You are now redirected to his linkdin profile.')
            save_command_to_excel(nam,query)
            webbrowser.open("https://www.linkedin.com/in/sripriya-agarwal-483475261/")
            redirect_to_google(query)
            break
thanos()