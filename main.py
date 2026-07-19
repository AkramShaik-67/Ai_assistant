import speech_recognition as sr
import pyttsx3
import pywhatkit 
import wikipedia
import pyjokes
import datetime
import webbrowser
import os
import pyautogui

# Voice engine 
listener = sr.Recognizer()

def talk(text):
    print("Bhai :", text)
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")
    
# Take command from user
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source,duration=1)
            
            voice = listener.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )
            print("Recognizing...")
            command = listener.recognize_google(voice)
            command = command.lower()
            
            print("You said: ", command)
    except:
        pass
    
    return command

# Main function
def run_bhai():
    command = take_command()
    
    # Play songs or videos on YouTube
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)
        
    # Get current time&date
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)
        
    elif "date" in command:
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        talk("Today's date is " + date)
    
    #Shutdown and Restart the computer
    elif "shutdown" in command:
        talk("Shutting down the computer")
        shutdown_path = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'System32', 'shutdown.exe')
        os.system(f'"{shutdown_path}" /s /t 1')
        
    elif "restart" in command:
        talk("Restarting the computer")
        shutdown_path = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'System32', 'shutdown.exe')
        os.system(f'"{shutdown_path}" /r /t 1')

    # Get a person's information from Wikipedia
    elif "who is" in command:
        person = command.replace("who is", "")
        try:
            info = wikipedia.summary(person, sentences=2)
            talk(info)
        except:
            talk("I couldn't find any information on that person.")
    # Get information on a topic from Wikipedia
    elif "what is" in command:
        topic = command.replace("what is", "")
        try:
            info = wikipedia.summary(topic, sentences=2)
            talk(info)
        except:
            talk("I couldn't find any information on that topic.")

    # Tell a joke
    elif "joke" in command:
        joke = pyjokes.get_joke()
        talk(joke)
        
    # Open YouTube
    elif "open youtube" in command:
        talk("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    # Open Google
    elif "open google" in command:
        talk("Opening Google")
        webbrowser.open("https://www.google.com")
    
    #Open Instagram
    elif "open instagram" in command:
        talk("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    
    #Open mail
    elif "open mail" in command:
        talk("Opening Gmail")
        webbrowser.open("https://mail.google.com")
    #Calculate
    elif "open calculator" in command or "calculator" in command or "calculate" in command:
        talk("Opening calculator")
        try:
            calc_path = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'System32', 'calc.exe')
            os.startfile(calc_path)
        except Exception:
            os.system("calc")
    
    #Open Notepad
    elif "open notepad" in command:
        talk("Opening Notepad")
        try:
            notepad_path = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'System32', 'notepad.exe')
            os.startfile(notepad_path)
        except Exception:
            os.system("notepad")

    # Open Stack Overflow
    elif "open stack overflow" in command:
        talk("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")
    
    #Screenshot
    elif "screenshot" in command:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        talk("Screenshot taken and saved as screenshot.png")
    
    #Exit
    elif "exit" in command or "stop" in command or "quit" in command or "bye" in command:
        talk("Goodbye! Have a great day!")
        exit()
    else:
        talk("I didn't understand that. Can you please repeat?")
    
#start the assistant
talk("Hello Akram, I am your assistant. How can I help you?") 

while True:
    run_bhai()