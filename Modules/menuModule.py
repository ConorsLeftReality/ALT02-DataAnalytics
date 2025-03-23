def Graphical_mainMenu():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Graphical Data Display Program\n")
    print("Menu:")
    print("Fixed Graphs\n")
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
    print("12. Jobs within a user defined job title")
    print("13. Jobs within a user defined company size")

    #select which graph to display
    menuSelection = input("Enter the graph you want to display\n:")
    if menuSelection >= "1" and menuSelection <= "13":
        print("Loading graph...")
        return menuSelection
    elif menuSelection >= "1" or menuSelection <= "13":
        print("Loading graph...")
        return menuSelection
    else:
        print("(New Achievement Unlocked: How did you get here?)\nSomething has broken in the Graph Input")
        print("Restart the program, if error persists, contact the developer.")
        exit()

def homeMenu():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Welcome to the Data Display Program, powered by the Pandas and Plotly Module\n")
    print("Menu:")
    print("1. Non-Graphical Data Display(Useful for non-graphical Operating Systems, or just data in text form)")
    print("2. Graphical Data Display (Requires Browser, no network connection required)")
    print("Or type 'exit' to exit the program")
    menuSelection = input("Enter the menu you want to access\n:")
    if menuSelection == "1":
        return "1"
    elif menuSelection == "2":
        return "2"
    elif menuSelection == "exit":
        return "exit"
    else:
        print("Invalid input, please enter a valid input")
        return "invalid"

def nonGraphical_mainMenu():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Non-Graphical Data Display Program\n")
    print("Menu:")
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

    menuSelection_nG = input("Enter the data you want to display\n:")
    if menuSelection_nG >= "1" and menuSelection_nG <= "16":
        print("Loading data...")
        return menuSelection_nG
    elif menuSelection_nG >= "1" or menuSelection_nG <= "16":  
        print("Loading data...")
        return menuSelection_nG
    else:
        print("(New Achievement Unlocked: How did you get here?)\nSomething has broken in the Data Input")
        print("If error persists, contact the developer.")
        return