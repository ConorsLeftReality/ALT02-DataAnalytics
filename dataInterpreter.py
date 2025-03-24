# Main Data Interpreter Program
# Talks to the Modules in moduleFolder
# Built for ALT02-Data Analytics as part of the Leaving Certificate Course
# With love by Conor Masterson

# Modules
import pandas as pd
import plotly.express as px
import time
import os
from Modules.dataModule import fileClean, dataInterprit_G, dataInterprit_nG
from Modules.menuModule import Graphical_mainMenu, homeMenu, nonGraphical_mainMenu, clearScreen
import webbrowser

def clearScreen(): # who doesnt like a clean terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
## !!!IMPORTANT!!!
## This module requires the modules folder to be present, as they are dependancies for this script
## if they arent present, they are accesible through https://github.com/ConorsLeftReality/ALT02-DataAnalytics

# Make cleaned data with dataModule, see how soon you need these dependancies
status, cleanedPath = fileClean()  # fileClean spits out whether cleaning was successful or not, and the cleaned file's path
if status == "quit":
    exit()
elif status == "success":
    print("Success, loading cleaned data...")
    time.sleep(0.5)
else:
    print("An error occured, likely with the dataModule or fileClean, please re-run the program")
    exit()

# Attempts to opens up cleaned data
try:
    df = pd.read_csv(cleanedPath)
# Error prints if you went wrong, because the user is always 100% right
except Exception as e:
    if "No such file or directory" in str(e):
        print(f"Error loading file: {e}\nWas the file name entered correctly?")
    else:
        print(f"Error loading file: {e}")
    exit()

# Displays menu for data display
exitProgram = False
while exitProgram == False:
    subMenuChoice = homeMenu()
    clearScreen()
    # User wants Non-Grapical Data
    if subMenuChoice == "1":
        print("Loading Non-Graphical Data Menu...")
        time.sleep(0.5)
        menuSelection_nG = nonGraphical_mainMenu()
        dataInterprit_nG(menuSelection_nG, df)
    # User wants Graphical Data
    elif subMenuChoice == "2":
        print("Loading Graphical Data Menu...")
        time.sleep(0.5)
        menuSelection = Graphical_mainMenu()
        dataInterprit_G(menuSelection, df)
    # User wants no more
    elif subMenuChoice == "quit":
        exitProgram = True
        clearScreen()
        print("Exiting program, thank you for using the Data Display Program!")
        exit()
    
    # Please dont mark me down on this
    elif subMenuChoice == "3": 
        clearScreen()
        print("New Achievement: How did we get here?")
        webbrowser.open("https://www.meme-arsenal.com/memes/242591b14631e9f3b858c3fff96f90af.jpg")
        time.sleep(5)
        # Forces Volume to 100%, thanks chatgpt
        if os.name == 'nt':
            os.system('powershell -Command "(New-Object -ComObject WScript.Shell).SendKeys([char]175)"')
        else:
            os.system('pactl set-sink-volume @DEFAULT_SINK@ 100%')
        webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")
        time.sleep(5)