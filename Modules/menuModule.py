def mainMenu():
    print("Welcome to the Data Display Program, powered by the Pandas and Plotly Module\n")
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
    if menuSelection > "13" or menuSelection < "1":
        return menuSelection
    elif menuSelection >= "1" and menuSelection <= "13":
        print("Loading graph...")
        return menuSelection
    else:
        print("(New Achievement Unlocked: How did you get here?)\nSomething has broken in the Graph Input")
        print("Restart the program, if error persists, contact the developer.")
        exit()