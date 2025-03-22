#alt02
#data should be cleaned prior to using this script, in form of .csv file and in the same location as this script (will be user confirmed)

#modules
import pandas as pd
import plotly.express as px

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Standard display of Data\n")
"""
originalPath = input("Enter the name of the file you want to display (Leave spaces out of the file name, type .csv at the end)\n:")
if file := originalPath[-4:] != ".csv":
    print("Please rerun the file and enter a valid .csv file")
    exit()

# attempt to load the file
try:
    df = pd.read_csv(originalPath)
except Exception as e:
    if "No such file or directory" in str(e):
        print(f"Error loading file: {e}\nWas the file name entered correctly?")
    else:
        print(f"Error loading file: {e}")
    exit()
"""
df = pd.read_csv('salaries_cleaned.csv')
# display menu for data display
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
print("User Defined Graphs\n")
print("9. Jobs within a user defined salary range") 
print("10. Jobs within a user defined experience range")
print("11. Jobs within a user defined country")
print("12. Jobs within a user defined job title")
print("13. Jobs within a user defined company size")

menuSelection = input("Enter the graph you want to display\n:")

if menuSelection == "1":
    AvgSal_Title = px.bar(df, x="salary_in_usd", y="job_title", title="Average Salary by Job Title")
    AvgSal_Title.show()
elif menuSelection == "2":
    AvgSal_Country = px.bar(df, x="employee_residence", y="Salary", title="Average Salary by Country of residence")
    AvgSal_Country.show()
elif menuSelection == "3":
    AvgSal_Exp = px.bar(df, x="experience_level", y="salary", title="Average Salary by Experience")
    AvgSal_Exp.show()
elif menuSelection == "4":
    AvgSal_Time = px.bar(df, x="work_year", y="salary", title="Average Salary over Time")
    AvgSal_Time.show()
elif menuSelection == "5":
    JobTitle_Amount = px.pie(df, names="job_title", title="Amount of Jobs by Title")
    JobTitle_Amount.show()
elif menuSelection == "6":
    Pay_highToLow = px.pie(df, names="job_title", values="salary", title="Highest and Lowest Paying Jobs")
    Pay_highToLow.show()
elif menuSelection == "7":
    Remote_Jobs = px.pie(df, names="remote_ratio", title="Number of Remote Jobs")
    Remote_Jobs.show()
elif menuSelection == "8":
    PartTime_FullTime = px.pie(df, names="employment_type", title="Part Time vs Full Time Jobs")
    PartTime_FullTime.show()
elif menuSelection == "9":
    salaryRange = input("Enter the salary range you want to display (e.g. 10000-20000)\n:")
    salaryRange = salaryRange.split("-")
    salaryRange = [int(i) for i in salaryRange]
    df = df[(df["Salary"] >= salaryRange[0]) & (df["Salary"] <= salaryRange[1])]
    SalaryRange = px.bar(df, x="Job Title", y="Salary", title="Jobs within a user defined salary range")
    SalaryRange.show()
elif menuSelection == "10":
    expRange = input("Enter the experience range you want to display (e.g. 1-3)\n:")
    expRange = expRange.split("-")
    expRange = [int(i) for i in expRange]
    df = df[(df["Experience"] >= expRange[0]) & (df["Experience"] <= expRange[1])]
    ExpRange = px.bar(df, x="Job Title", y="Salary", title="Jobs within a user defined experience range")
    ExpRange.show()
elif menuSelection == "11":
    country = input("Enter the country you want to display\n:")
    df = df[df["Country"] == country]
    Country = px.bar(df, x="Job Title", y="Salary", title="Jobs within a user defined country")
    Country.show()
elif menuSelection == "12":
    jobTitle = input("Enter the job title you want to display\n:")
    df = df[df["Job Title"] == jobTitle]
    JobTitle = px.bar(df, x="Job Title", y="Salary", title="Jobs within a user defined job title")
    JobTitle.show()
elif menuSelection == "13":
    companySize = input("Enter the company size you want to display\n:")
    df = df[df["Company Size"] == companySize]
    CompanySize = px.bar(df, x="Job Title", y="Salary", title="Jobs within a user defined company size")
    CompanySize.show()
else:
    print("Invalid selection, please re-run the program and enter a valid selection")
    exit()