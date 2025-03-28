#Dependancies
import os
import time

def clearScreen(): # who doesnt like a clean terminal
    print("\n=================================================\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    
def logo():
    print(r"______      _          _____      _                           _            ")
    print(r"|  _  \    | |        |_   _|    | |                         | |           ")
    print(r"| | | |__ _| |_ __ _    | | _ __ | |_ ___ _ __ _ __  _ __ ___| |_ ___ _ __ ")
    print(r"| | | / _` | __/ _` |   | || '_ \| __/ _ | '__| '_ \| '__/ _ | __/ _ | '__|")
    print(r"| |/ | (_| | || (_| |  _| || | | | ||  __| |  | |_) | | |  __| ||  __| |   ")
    print(r"|___/ \__,_|\__\__,_|  \___|_| |_|\__\___|_|  | .__/|_|  \___|\__\___|_|   ")
    print(r"                                              | |                          ")
    print(r"                                              |_|                          ")
    print(r"")
    
def homeMenu():
    subMenuList = ["1","2","quit","3"]
    # Clear the screen
    clearScreen()
    # Prints menu
    logo()
    print("========================== Home Menu ===========================")
    print("1. Non-Graphical Menu (For non graphical OS or pandas only data)")
    print("2. Graphical Menu (Requires Browser, doesnt require Network)")
    print("             Or just type 'quit' to quit the program.\n         ")
    
    submenuSelection = input("|Type here| ")
    # Check for valid selection, else re-prompt
    while (submenuSelection in subMenuList) == False:
        clearScreen()
        logo()
        print("========================== Home Menu ===========================")
        print("1. Non-Graphical Menu (For non graphical OS or pandas only data)")
        print("2. Graphical Menu (Requires Browser, doesnt require Network)")
        print("             Or just type 'quit' to quit the program.\n         ")
        submenuSelection = input("|Invalid selection - Make a valid selection| ")
    return submenuSelection

def Graphical_mainMenu():
    # Makes List, string of 1 to 13 (range goes to nMax-1)
    G_List = [str(i) for i in range(1, 14)] + ["back"]
    # Clear the screen
    clearScreen()
    # Prints menu
    print("Graphical Data Display\n")
    print("Fixed Graphs")
    print("1. Average salary by job title")
    print("2. Average salary by country(in USD)")
    print("3. Average salary by experience")
    print("4. Average salary over time (Bar Graph)")
    print("5. Amount of jobs by title")
    print("6. Highest paying job and lowest paying job")
    print("7. Number of remote jobs (by remote ratio)")
    print("8. Part time vs Full time jobs")
    print("\nUser Defined Graphs")
    print("9. Jobs within a user defined salary range") 
    print("10. Jobs within a user defined experience range")
    print("11. Jobs within a user defined country")
    print("12. Jobs within a user defined company size")
    print("Or 'back' to return to main menu")
    
    menuSelection = input("Make a selection: ")
    # Check for valid selection, else re-prompt
    while (menuSelection in G_List) == False:
        menuSelection = input("Invalid selection - Make a valid selection: ")
    return menuSelection

def nonGraphical_mainMenu():
    # Makes List, same as comment on Graphical, but its for 1-16
    nG_List = [str(i) for i in range(1, 17)] + ["back"]
    # clear the screen
    clearScreen()
    # print menu
    print("Non-Graphical Data Display\n")
    print("Mean:")
    print("1. Mean salary by title")
    print("2. Mean salary by country")
    print("3. Mean salary by experience")
    print("4. Mean salary over time\n")
    print("Mode:")
    print("5. Mode of job title")
    print("6. Mode of Experience")
    print("7. Mode of Countries worked")
    print("8. Mode of Countries lived in\n")
    print("Median:")
    print("9. Median salary by title")
    print("10. Median salary by country")
    print("11. Median salary by experience")
    print("12. Median salary over time\n")
    print("Range:")
    print("13. Range of Pay")
    print("14. Range of Pay by User Defined Country")
    print("15. Range of Pay by User Defined Title")
    print("16. Range of Pay by User Defined Experience\n")
    print("Or 'back' to return to main menu")
    
    menuSelection_nG = input("Make a Selection: ")
    # Check for valid selection, else re-prompt
    while (menuSelection_nG in nG_List) == False:
          menuSelection_nG = input("Invalid selection - Make a valid selection: ")
    return menuSelection_nG