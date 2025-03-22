#alt02
#data should be cleaned prior to using this script, in form of .csv file and in the same location as this script (will be user confirmed)

#modules
import pandas as pd
import plotly.express as px
import time
from Modules.dataModule import fileClean
from Modules.menuModule import mainMenu

#get cleaned data
status, cleanedPath = fileClean()
if status == "failed":
    print("Please restart the program and enter a valid file")
    exit()
elif status == "success":
    print("Success, loading cleaned data...")
    time.sleep(1)
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
    menuSelection = mainMenu()

    if menuSelection == "1":
        AvgSal_Title = px.bar(df, x="salary_in_usd", y="job_title", title="Average Salary by Job Title")
        AvgSal_Title.show()
        time.sleep(2)
    elif menuSelection == "2":
        AvgSal_Country = px.bar(df, x="employee_residence", y="salary_in_usd", title="Average Salary by Country")
        AvgSal_Country.show()
        time.sleep(2)
    elif menuSelection == "3":
        AvgSal_Exp = px.bar(df, x="experience_level", y="salary_in_usd", title="Average Salary by Experience")
        AvgSal_Exp.show()
        time.sleep(2)
    elif menuSelection == "4":
        AvgSal_Time = px.bar(df, x="work_year", y="salary_in_usd", title="Average Salary over Time")
        AvgSal_Time.show()
        time.sleep(2)
    elif menuSelection == "5":
        JobTitle_Amount = px.pie(df, names="job_title", title="Amount of Jobs by Title")
        JobTitle_Amount.show()
        time.sleep(2)
    elif menuSelection == "6":
        Pay_highToLow = px.pie(df, names="job_title", values="salary_in_usd", title="Highest and Lowest Paying Jobs")
        Pay_highToLow.show()
        time.sleep(2)
    elif menuSelection == "7":
        Remote_Jobs = px.pie(df, names="remote_ratio", title="Number of Remote Jobs")
        Remote_Jobs.show()
        time.sleep(2)
    elif menuSelection == "8":
        PartTime_FullTime = px.pie(df, names="employment_type", title="Part Time vs Full Time Jobs")
        PartTime_FullTime.show()
        time.sleep(2)

    # User Defined Graphs
    elif menuSelection == "9":
        salaryRange = input("Enter the salary range you want to display (e.g. 10000-20000)\n:")
        salaryRange = salaryRange.split("-")
        salaryRange = [int(i) for i in salaryRange]
        df_filtered = df[(df["salary_in_usd"] >= salaryRange[0]) & (df["salary_in_usd"] <= salaryRange[1])]
        SalaryRange = px.bar(df_filtered, x="job_title", y="salary_in_usd", title="Jobs within a user defined salary range")
        SalaryRange.show()
        time.sleep(2)
    elif menuSelection == "10":
        expRange = input("Enter the experience range you want to display (e.g. 1-3)\n:")
        expRange = expRange.split("-")
        expRange = [int(i) for i in expRange]
        df_filtered = df[(df["experience_level"] >= expRange[0]) & (df["experience_level"] <= expRange[1])]
        ExpRange = px.bar(df_filtered, x="job_title", y="salary_in_usd", title="Jobs within a user defined experience range")
        ExpRange.show()
        time.sleep(2)
    elif menuSelection == "11":
        country = input("Enter the country you want to display\n:")
        df_filtered = df[df["employee_residence"] == country]
        Country = px.bar(df_filtered, x="job_title", y="salary_in_usd", title="Jobs within a user defined country")
        Country.show()
        time.sleep(2)
    elif menuSelection == "12":
        jobTitle = input("Enter the job title you want to display\n:")
        df_filtered = df[df["job_title"] == jobTitle]
        JobTitle = px.bar(df_filtered, x="job_title", y="salary_in_usd", title="Jobs within a user defined job title")
        JobTitle.show()
        time.sleep(2)
    elif menuSelection == "13":
        companySize = input("Enter the company size you want to display\n:")
        df_filtered = df[df["company_size"] == companySize]
        CompanySize = px.bar(df_filtered, x="job_title", y="salary_in_usd", title="Jobs within a user defined company size")
        CompanySize.show()
        time.sleep(2)
    elif menuSelection == "exit":
        exitProgram = True
        print("Exiting program, thank you for using the Data Display Program!")
        exit()
    else:
        print("Invalid selection")
        time.sleep(1)