#dependancies
import pandas as pd
import plotly.express as px
import time
import os

def clearScreen(): # declutters
    os.system('cls' if os.name == 'nt' else 'clear')

def loadAnimation():
    print(".")
    time.sleep(0.2)
    clearScreen()
    print("..")
    time.sleep(0.2)
    clearScreen()
    print("...")
    time.sleep(0.2)
    clearScreen()
    print(".")
    time.sleep(0.2)
    clearScreen()
    print("..")
    time.sleep(0.2)
    clearScreen()
    print("...")
    time.sleep(0.2)
    clearScreen()
    print(".")
    time.sleep(0.2)
    clearScreen()
    print("..")
    time.sleep(0.2)
    clearScreen()
    print("...")
    time.sleep(0.2)
    clearScreen()
    return

#file cleaner function, drops all rows with missing values, all duplicated rows and rows with NULL values
def fileClean():
    # Clears the Screen
    clearScreen()
    # Asks user for the name (path) of the .csv file)
    originalPath = input("Enter the name of the file you want to clean (Leave spaces out of the file name, type .csv at the end)\n: ")
    # Checks if path contains .csv at the end
    while originalPath[-4:] != ".csv" or len(originalPath)== 4:
        clearScreen()
        originalPath = input("Enter the name of a valid file you want to clean (Leave spaces out of the file name, type .csv at the end)\n: ")
    # Once originalPath contains .csv at the end, it opens file as a dataframe
    df = pd.read_csv(originalPath)
    #prints a sample of the dataframe
    clearScreen()
    print(df.sample(5))
    rightFileConfirm = input("Is this the correct file? (Check columns, tables, etc.)(y/N)\n: ").lower()
    # Is the input valid?
    while rightFileConfirm != "y" and rightFileConfirm != "n":
        print("Invalid Input")
        rightFileConfirm = input("Is this the correct file? (Check columns, tables, etc.)(y/n)\n: ").lower()
    # File isnt correct
    if rightFileConfirm == "n":
        print("Ending program...")
        return "quit", ""
    # File correct
    elif rightFileConfirm == "y":
        print("Cleaning file...")
        df = df.dropna()
        df = df.drop_duplicates()
        if 'salary ' in df.columns:
            df = df[df['salary'] <= 400000]
        #making cleaned path
        cleanedPath = (originalPath[:-4] + "_cleaned.csv")
        df.to_csv(cleanedPath, index=False)
        print("File cleaned and saved as " + cleanedPath)
        return "success", cleanedPath
    
def dataInterprit_G(menuSelection, df):
    if menuSelection == "1":
        AvgSal_Title = px.bar(df, x="salary_in_usd", y="job_title", title="Average Salary by Job Title")
        AvgSal_Title.show()
        loadAnimation()
    elif menuSelection == "2":
        AvgSal_Country = px.bar(df, x="employee_residence", y="salary_in_usd", title="Average Salary by Country")
        AvgSal_Country.show()
        loadAnimation()
    elif menuSelection == "3":
        AvgSal_Exp = px.bar(df, x="experience_level", y="salary_in_usd", title="Average Salary by Experience")
        AvgSal_Exp.show()
        loadAnimation()
    elif menuSelection == "4":
        AvgSal_Time = px.bar(df, x="work_year", y="salary_in_usd", title="Average Salary over Time")
        AvgSal_Time.show()
        loadAnimation()
    elif menuSelection == "5":
        JobTitle_Amount = px.pie(df, names="job_title", title="Amount of Jobs by Title")
        JobTitle_Amount.show()
        loadAnimation()
    elif menuSelection == "6":
        Pay_highToLow = px.pie(df, names="job_title", values="salary_in_usd", title="Highest and Lowest Paying Jobs")
        Pay_highToLow.show()
        loadAnimation()
    elif menuSelection == "7":
        Remote_Jobs = px.pie(df, names="remote_ratio", title="Number of Remote Jobs")
        Remote_Jobs.show()
        loadAnimation()
    elif menuSelection == "8":
        PartTime_FullTime = px.pie(df, names="employment_type", title="Part Time vs Full Time Jobs")
        PartTime_FullTime.show()
        loadAnimation()

    # User Defined Graphs
    elif menuSelection == "9":
        salaryRange = input("Enter the salary range you want to display (e.g. 10000-20000)\n:")
        salaryRange = salaryRange.split("-")
        salaryRange = [int(i) for i in salaryRange]
        df_filtered = df[(df["salary_in_usd"] >= salaryRange[0]) & (df["salary_in_usd"] <= salaryRange[1])]
        SalaryRange = px.bar(df_filtered, x="job_title", y="salary_in_usd", title="Jobs within a user defined salary range")
        SalaryRange.show()
        loadAnimation()
    elif menuSelection == "10":
        expRange = input("Enter the experience range you want to display (e.g. 1-3)\n:")
        expRange = expRange.split("-")
        expRange = [int(i) for i in expRange]
        df_filtered = df[(df["experience_level"] >= expRange[0]) & (df["experience_level"] <= expRange[1])]
        ExpRange = px.bar(df_filtered, x="job_title", y="salary_in_usd", title="Jobs within a user defined experience range")
        ExpRange.show()
        loadAnimation()
    elif menuSelection == "11":
        country = input("Enter the country you want to display\n:")
        df_filtered = df[df["employee_residence"] == country]
        Country = px.bar(df_filtered, x="job_title", y="salary_in_usd", title="Jobs within a user defined country")
        Country.show()
        loadAnimation()
    elif menuSelection == "12":
        jobTitle = input("Enter the job title you want to display\n:")
        df_filtered = df[df["job_title"] == jobTitle]
        JobTitle = px.bar(df_filtered, x="job_title", y="salary_in_usd", title="Jobs within a user defined job title")
        JobTitle.show()
        loadAnimation()
    elif menuSelection == "13":
        companySize = input("Enter the company size you want to display\n:")
        df_filtered = df[df["company_size"] == companySize]
        CompanySize = px.bar(df_filtered, x="job_title", y="salary_in_usd", title="Jobs within a user defined company size")
        CompanySize.show()
        loadAnimation()
    elif menuSelection == "exit":
        exitProgram = True
        print("Exiting program, thank you for using the Data Display Program!")
        exit()
    else:
        print("Invalid selection")
        time.sleep(1)
    return
def dataInterprit_nG(menuSelection, df):
    print("Work In Progress")
    # write this using only pandas, no plotly as it requires graphics
    # # Terminal Lives Matter
    time.sleep(2)