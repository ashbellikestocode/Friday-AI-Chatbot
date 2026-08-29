import datetime
import webbrowser
import subprocess
from speech import speak


#The main Brain Function
def process_command(recognized_command):
    if "time" in recognized_command:
       time=get_time()
       speak(time)
    elif "google" in recognized_command:
        speak("Opening Google...")
        open_google()
    elif "spotify" in recognized_command:
        print("opening spotify")
        open_spotify()
    elif "youtube" in recognized_command:
        speak("opening youtube")
        open_youtube()
    elif "chat gpt" in recognized_command:
        speak("opening chatgpt")
        open_chatgpt()
    elif "chrome" in recognized_command:
        speak("print opening chrome")
        open_chrome()
        
        

def get_time():
    current_time=datetime.datetime.now()
    formatted_time=current_time.strftime("%I:%M %p")
    return formatted_time


def open_google():
    webbrowser.open("https://www.google.com")

def open_spotify():
    webbrowser.open("https://open.spotify.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_chatgpt():
    webbrowser.open("https://chatgpt.com/")

def open_chrome():
    subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
