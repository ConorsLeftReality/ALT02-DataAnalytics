#alt02
#data should be cleaned prior to using this script, in form of .csv file and in the same location as this script (will be user confirmed)

#modules
import pandas as pd
import plotly.express as px
import time
from Modules.dataModule import fileClean, dataInterprit_G, dataInterprit_nG
from Modules.menuModule import Graphical_mainMenu, homeMenu, nonGraphical_mainMenu

#get cleaned data
status, cleanedPath = fileClean()
if status == "failed":
    print("Please restart the program and enter a valid file")
    exit()
elif status == "success":
    print("Success, loading cleaned data...")
    time.sleep(1)
elif status == "loop":
    print("Please restart the program and enter a valid file")
    exit()
else:
    print("An error occured, likely with the dataModule or fileClean, please re-run the program")
    exit()

# opens up cleaned data
try:
    df = pd.read_csv(cleanedPath)
except Exception as e:
    if "No such file or directory" in str(e):
        print(f"Error loading file: {e}\nWas the file name entered correctly?")
    else:
        print(f"Error loading file: {e}")
    exit()

# display menu for data display
exitProgram = False
while exitProgram == False:
    subMenuChoice = homeMenu()
    if subMenuChoice == "1":
        print("Loading Non-Graphical Data Display...")
        time.sleep(1)
        menuSelection_nG = nonGraphical_mainMenu()
        dataInterprit_nG(menuSelection_nG, df)
    elif subMenuChoice == "2":
        print("Loading Graphical Data Display...")
        time.sleep(1)
        menuSelection = Graphical_mainMenu()
        dataInterprit_G(menuSelection, df)
    elif subMenuChoice == "exit":
        exitProgram = True
        print("Exiting program, thank you for using the Data Display Program!")
        exit()
    else:
        print("Invalid input, please restart the program and enter a valid input")