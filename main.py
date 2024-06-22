import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import tkinter as tk

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tellTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is " + hour + " Hours and " + min + " Minutes")


def Hello():
    speak("hello sir I am your desktop assistant. Tell me how may I help you")


def openGeeksForGeeks():
    speak("Opening GeeksforGeeks")
    webbrowser.open("https://www.geeksforgeeks.org")


def openGoogle():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")


def searchWikipedia(query):
    speak("Checking Wikipedia")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=4)
    speak("According to Wikipedia")
    speak(result)


def create_gui():
    window = tk.Tk()
    window.title("Desktop Assistant")

    label = tk.Label(window, text="Assistant Commands:", font=("Arial", 14))
    label.pack()

    geeksforgeeks_button = tk.Button(window, text="Open GeeksforGeeks", command=openGeeksForGeeks)
    geeksforgeeks_button.pack()

    google_button = tk.Button(window, text="Open Google", command=openGoogle)
    google_button.pack()

    wikipedia_entry = tk.Entry(window, width=50)
    wikipedia_entry.pack()

    search_button = tk.Button(window, text="Search Wikipedia", command=lambda: searchWikipedia(wikipedia_entry.get()))
    search_button.pack()

    window.mainloop()


def Take_query():
    Hello()
    while True:
        query = takeCommand().lower()
        if "open geeksforgeeks" in query:
            openGeeksForGeeks()
        elif "open google" in query:
            openGoogle()
        elif "which day it is" in query:
            tellDay()
        elif "tell me the time" in query:
            tellTime()
        elif "bye" in query:
            speak("Bye. Check Out GFG for more exciting things")
            exit()
        elif "from wikipedia" in query:
            searchWikipedia(query)
        elif "tell me your name" in query:
            speak("I am Jarvis. Your desktop Assistant")


if __name__ == '__main__':
    create_gui()
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
