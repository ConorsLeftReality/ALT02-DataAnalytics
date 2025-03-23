#alt02
#data should be cleaned prior to using this script, in form of .csv file and in the same location as this script (will be user confirmed)

#modules
import pandas as pd
import plotly.express as px
import time
import os
from Modules.dataModule import fileClean, dataInterprit_G, dataInterprit_nG
from Modules.menuModule import Graphical_mainMenu, homeMenu, nonGraphical_mainMenu, clearScreen
    
# get cleaned data
status, cleanedPath = fileClean()  #fileclean spits out whether cleaning was successful or not, and the cleaned file's path
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
    # User has had enough.
    elif subMenuChoice == "quit":
        exitProgram = True
        print("Exiting program, thank you for using the Data Display Program!")
        exit()