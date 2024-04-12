import datetime
import os
import random
import string
import webbrowser
import pandas as pd
import pyttsx3
import speech_recognition as sr


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
def get_random_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta.",
        "How do you organize a fantastic space party? You planet!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
        "Why did the bicycle fall over? Because it was two-tired!",
        "How do you catch a squirrel? Climb a tree and act like a nut!",
        "What did one hat say to the other? Stay here, I'm going on ahead!",
        "Why did the scarecrow become a successful motivational speaker? Because he was outstanding in his field!",
        "How do you make a tissue dance? You put a little boogie in it.",
        "What did one ocean say to the other ocean? Nothing, they just waved.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What's a vampire's favorite fruit? A blood orange.",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
        "Why don't oysters donate to charity? Because they are shellfish.",
        "How does a penguin build its house? Igloos it together!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "Why did the coffee file a police report? It got mugged.",
        "How do you organize a space party? You planet!",
        "Why did the computer go to therapy? Because it had too many bytes of emotional baggage.",
        "What do you call a fish wearing a crown? A kingfish.",
        "Why don't seagulls fly over the bay? Because then they'd be bagels.",
        "What do you call a fake noodle? An impasta.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What did one wall say to the other wall? I'll meet you at the corner.",
        "How do you catch a squirrel? Climb a tree and act like a nut!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What did one hat say to the other? Stay here, I'm going on ahead!",
        "Why did the math book look sad? Because it had too many problems.",
        "What's orange and sounds like a parrot? A carrot.",
        "Why did the scarecrow become a successful motivational speaker? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What did one ocean say to the other ocean? Nothing, they just waved.",
        "Why did the chicken go to the seance? To talk to the other side.",
        "How do you make a tissue dance? You put a little boogie in it.",
        "Why don't eggs tell each other secrets? Because they might crack up.",
        "What did the janitor say when he jumped out of the closet? Supplies!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How do you organize a fantastic space party? You planet!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "How do you catch a squirrel? Climb a tree and act like a nut!",
        "What did one hat say to the other? Stay here, I'm going on ahead!",
        "Why did the scarecrow become a successful motivational speaker? Because he was outstanding in his field!",
        "How do you make a tissue dance? You put a little boogie in it.",
        "What did one ocean say to the other ocean? Nothing, they just waved.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What's a vampire's favorite fruit? A blood orange.",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
        "Why don't oysters donate to charity? Because they are shellfish.",
        "How does a penguin build its house? Igloos it together!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "Why did the coffee file a police report? It got mugged.",
        "How do you organize a space party? You planet!",
        "Why did the computer go to therapy? Because it had too many bytes of emotional baggage.",
        "What do you call a fish wearing a crown? A kingfish.",
        "Why don't seagulls fly over the bay? Because then they'd be bagels.",
        "What do you call a fake noodle? An impasta.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What did one wall say to the other wall? I'll meet you at the corner.",
        "How do you catch a squirrel? Climb a tree and act like a nut!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What did one hat say to the other? Stay here, I'm going on ahead!",
        "Why did the math book look sad? Because it had too many problems.",
        "What's orange and sounds like a parrot? A carrot.",
        "Why did the scarecrow become a successful motivational speaker? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What did one ocean say to the other ocean? Nothing, they just waved.",
        "Why did the chicken go to the seance? To talk to the other side.",
        "How do you make a tissue dance? You put a little boogie in it.",
        "Why don't eggs tell each other secrets? Because they might crack up.",
        "What did the janitor say when he jumped out of the closet? Supplies!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How do you organize a fantastic space party? You planet!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "How do you catch a squirrel? Climb a tree and act like a nut!",
        "What did one hat say to the other? Stay here, I'm going on ahead!",
        "Why did the scarecrow become a successful motivational speaker? Because he was outstanding in his field!",
        "How do you make a tissue dance? You put a little boogie in it.",
        "What did one ocean say to the other ocean? Nothing, they just waved.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What's a vampire's favorite fruit? A blood orange"]
    return random.choice(jokes)
def take_name():
    while True:
        say("Please tell me your name")
        nam = takecommand()
        if nam:
            say(f"Hello, {nam}! How may I help you today?")
            print("Try Saying 'tell me a joke' ")
            return nam
def save_command_to_excel(name, command):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {'Name': name, 'Date': current_date, 'Command': command}
    df = pd.DataFrame(data, index=[0])

    try:
        existing_data = pd.read_excel('user_commands.xlsx')
        df = pd.concat([existing_data, df], ignore_index=True)
    except Exception as a_1:
        print(f"Error saving data to Excel: {a_1}")

    df.to_excel('user_commands.xlsx', index=False)

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

        if "play music".lower() in query.lower() or "gana bajao".lower() in query.lower():
            musicpath = r"C:\Users\RAHUL\Downloads\starboy.mp3"
            os.startfile(musicpath)
            should_continue = False
        elif "play bhajan".lower() in query.lower() or "bhajan bajao".lower() in query.lower() or "bhajan sunao".lower() in query.lower():
            bhajanpath = r"C:\Users\RAHUL\Downloads\bhajan.mp3"
            os.startfile(bhajanpath)
            should_continue = False

        elif "what is time".lower() in query or "time bata".lower() in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f" Sir current time is {hour}baj ke {min} minutes, but your time is bad since you took engineering ")
            should_continue = False
        elif "how r u" in query.lower() or "how are you" in query.lower() or "kaise ho tum" in query.lower() or "kaise ho" in query.lower() or "kya hal" in query.lower() :
            say("My mood is going to be displayed shortly")
            webbrowser.open("https://www.youtube.com/shorts/tzJuDQnNnkY")
            should_continue = False
        elif "what is your mood".lower() in query.lower() or "mood".lower() in query.lower():
            say ("My mood is moye moye")
            moyepath = r"C:\Users\RAHUL\Downloads\moye moye.mp3"
            os.startfile(moyepath)
            should_continue = False
        # if "Tell me a joke".lower() in query.lower() or "Chutkula sunao".lower() in query.lower():
        #     say("I will show you the biggest joke nearby")
        #     camera = r"C:\Program Files\WindowsApps\Microsoft.WindowsCamera_2023.2311.5.0_x64__8wekyb3d8bbwe\WindowsCamera.exe"
        #     os.startfile(camera)
        #     should_continue = False
        # elif "wire industry".lower() in query.lower() or "cable industry".lower() in query.lower() or "wire and cable industry".lower() in query:
        #     say("Sure sir, here are the details on google")
        #     webbrowser.open("https://www.google.com/search?q=all+about+wire+and+cable+industry&rlz=1C1RXQR_en-GBIN1069IN1069&oq=all+about+wire+and+cable+industry+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigATIHCAUQIRigATIKCAYQIRgWGB0YHjIKCAcQIRgWGB0YHjIKCAgQIRgWGB0YHjIKCAkQIRgWGB0YHtIBCTEyODA2ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
        #     should_continue = False
        elif  "tell me a joke".lower() in query.lower() or "joke".lower() in query.lower() or "make me laugh".lower() in query.lower() :
            say("Sure sir")
            say("I am thinking of a joke")
            say("here's one")
            say(get_random_joke())
            should_continue = False
        elif "maths problem".lower() in query.lower() or "math question".lower() in query.lower() or "maths questons".lower() in query or "maths problems".lower() in query or "math problem".lower() in query :
            say("Ohh! Problem, nahh! Major problem, a maths problem detected.")
            say("Internet will solve it for you.")
            webbrowser.open("https://math.microsoft.com/en")
            should_continue = False

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