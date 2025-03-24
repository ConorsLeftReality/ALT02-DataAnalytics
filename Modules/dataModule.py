#dependancies
import pandas as pd
import plotly.express as px
import time
import os

#clearScreen redefined because import module issues in thonny
def clearScreen(): # who doesnt like a clean terminal
    print("\n=================================================\n")
    os.system('cls' if os.name == 'nt' else 'clear')

# variables used later on for displaying the jobs list, as there are a lot of job titles
startIndex_global = 0 # originally starts at start of list
batchSize = 5 # displays 5 at a time

# Dictionary for Country conversions later
countryDictionary = {
    'Netherlands': 'NL', 'United States': 'US', 'United Kingdom': 'GB', 'Lithuania': 'LT',
    'Canada': 'CA', 'Spain': 'ES', 'Germany': 'DE', 'Latvia': 'LV', 'Belgium': 'BE',
    'France': 'FR', 'Slovakia': 'SK', 'Philippines': 'PH', 'Ireland': 'IE', 'Australia': 'AU',
    'Brazil': 'BR', 'India': 'IN', 'Poland': 'PL', 'Peru': 'PE', 'Argentina': 'AR', 'Austria': 'AT',
    'Switzerland': 'CH', 'New Zealand': 'NZ', 'Portugal': 'PT', 'Serbia': 'RS', 'Finland': 'FI',
    'Taiwan': 'TW', 'Norway': 'NO', 'Ukraine': 'UA', 'El Salvador': 'SV', 'Ecuador': 'EC',
    'Chile': 'CL', 'Dominican Republic': 'DO', 'Mexico': 'MX', 'Colombia': 'CO', 'Malta': 'MT',
    'Denmark': 'DK', 'Indonesia': 'ID', 'Malaysia': 'MY', 'Kosovo': 'XK', 'Costa Rica': 'CR',
    'Japan': 'JP', 'Zambia': 'ZM', 'Puerto Rico': 'PR', 'Armenia': 'AM', 'Singapore': 'SG',
    'Luxembourg': 'LU', 'Italy': 'IT', 'Cyprus': 'CY', 'Congo (Democratic Republic)': 'CD',
    'Israel': 'IL', 'Czech Republic': 'CZ', 'South Korea': 'KR', 'South Africa': 'ZA', 'Egypt': 'EG',
    'Lebanon': 'LB', 'Greece': 'GR', 'Nigeria': 'NG', 'Bulgaria': 'BG', 'Hungary': 'HU', 'Croatia': 'HR',
    'Kenya': 'KE', 'Sweden': 'SE', 'Turkey': 'TR', 'Pakistan': 'PK', 'Honduras': 'HN', 'Romania': 'RO',
    'Venezuela': 'VE', 'Algeria': 'DZ', 'American Samoa': 'AS', 'United Arab Emirates': 'AE',
    'Saudi Arabia': 'SA', 'Oman': 'OM', 'Bosnia and Herzegovina': 'BA', 'Estonia': 'EE', 'Vietnam': 'VN',
    'Gibraltar': 'GI', 'Slovenia': 'SI', 'Mauritius': 'MU', 'Russia': 'RU', 'Qatar': 'QA', 'Ghana': 'GH',
    'Andorra': 'AD', 'Hong Kong': 'HK', 'Central African Republic': 'CF', 'Thailand': 'TH', 'Iran': 'IR',
    'Bahamas': 'BS', 'Iraq': 'IQ', 'China': 'CN', 'Moldova': 'MD'
}

# making jobTitle List not hardcoded
jobTitles_list = []

def countryList():
    i=0
    countries_per_line=5
    for country in countryDictionary:
        i+=1
        print(country,end="")
        ## Print several countries per line
        if (i % countries_per_line == 0):
            print()
        else:
            print(", ",end="")

def experienceDisplay():
    print("EN. Entry-level / Junior\nMI.  Mid-level / Intermediate\nSE. Senior-level / Expert\nEX. Executive-level / Director")

experienceList = ['EN','MI','SE','EX'] # list to verify function with
def country_ISO_Convert(countryName):
    countryName = countryName.strip().title()  # ALL CAPS WHEN YOU SPELL THE MANS NAME
    return countryDictionary.get(countryName, "Country not found")

def jobsListDisplay(batchSize, startIndex): # Batch Jobs display for nG data interpretation
    # Print the next batch of items
    clearScreen()
    result = "kjsadbfd"
    for i in range(startIndex, startIndex + batchSize):
            print(jobTitles_list[i]) # prints 5 new jobs
    while result not in jobTitles_list and result != "more":
        clearScreen()
        for i in range(startIndex, startIndex + batchSize):
            print(jobTitles_list[i]) # prints 5 new jobs
        result = input("Enter exact Job title, or 'more' for 5 more titles: ")
    return result,(startIndex + batchSize) # receiving side of code will call this the new startIndex
    
def loadAnimation(): # swag
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

def pause():
    input("Press enter to return to main menu")
    
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
        if 'salary_in_usd' in df.columns:
            df = df[df['salary_in_usd'] <= 500000] 
            df = df[df['salary_in_usd'] > 10000]
        #making cleaned path
        cleanedPath = (originalPath[:-4] + "_cleaned.csv")
        df.to_csv(cleanedPath, index=False)
        # create jobTitles_list for later, reduces hard-coded data
        global jobTitles_list
        jobTitles_list = df['job_title'].unique()
        return "success", cleanedPath

#################################################################################################################################################################

def dataInterprit_G(menuSelection, df):
    if menuSelection == "1":
        clearScreen()
        AvgSal_TitleGrouping = df.groupby('job_title')['salary_in_usd'].mean().reset_index()
        AvgSal_TitleGrouping['salary_in_usd'] = AvgSal_TitleGrouping['salary_in_usd'].round(2)
        AvgSal_Title = px.bar(AvgSal_TitleGrouping, x="job_title", y="salary_in_usd", title="Average Salary by Job Title")
        AvgSal_Title.show()
        loadAnimation()
    elif menuSelection == "2":
        clearScreen()
        AvgSal_CountryGrouping = df.groupby('company_location')['salary_in_usd'].mean().reset_index()
        AvgSal_CountryGrouping['salary_in_usd'] = AvgSal_CountryGrouping['salary_in_usd'].round(2)
        AvgSal_Country = px.bar(AvgSal_CountryGrouping, x="company_location", y="salary_in_usd", title="Average Salary by Business Country (ISO 3166 Format)")
        AvgSal_Country.show()
        loadAnimation()
    elif menuSelection == "3":
        clearScreen()
        AvgSal_ExpGrouping = df.groupby('experience_level')['salary_in_usd'].mean().reset_index()
        AvgSal_ExpGrouping['salary_in_usd'] = AvgSal_ExpGrouping['salary_in_usd'].round(2)
        AvgSal_Exp = px.bar(AvgSal_ExpGrouping, x="experience_level", y="salary_in_usd", title="Average Salary by Experience")
        AvgSal_Exp.show()
        loadAnimation()
    elif menuSelection == "4":
        clearScreen()
        AvgSal_TimeGrouping = df.groupby('work_year')['salary_in_usd'].mean().reset_index()
        AvgSal_TimeGrouping['salary_in_usd'] = AvgSal_TimeGrouping['salary_in_usd'].round(2)
        AvgSal_Time = px.line(AvgSal_TimeGrouping, x="work_year", y="salary_in_usd", title="Average Salary over Time")
        AvgSal_Time.show()
        loadAnimation()
    elif menuSelection == "5":
        clearScreen()
        # Filter job titles so we get jobs that are greater than 1%, as plot didnt display well with lots of small percentages
        jobCounts = df['job_title'].value_counts(normalize=True)
        filteredJobs = jobCounts[jobCounts > 0.01].index
        dfFiltered = df[df['job_title'].isin(filteredJobs)]
        JobTitle_Amount = px.pie(dfFiltered, names="job_title", title="Top Amount of Jobs by Title")
        JobTitle_Amount.show()
        loadAnimation()
    elif menuSelection == "6":
        clearScreen()
        # Turns out plotly really doesnt like lots of small numbers
        jobCounts = df['job_title'].value_counts(normalize=True)
        filteredJobs = jobCounts[jobCounts > 0.01].index
        dfFiltered = df[df['job_title'].isin(filteredJobs)]
        Pay_highToLow = px.pie(dfFiltered, names="job_title", values="salary_in_usd", title="Top Highest Paying Jobs")
        Pay_highToLow.show()
        loadAnimation()
    elif menuSelection == "7":
        clearScreen()
        Remote_Jobs = px.pie(df, names="remote_ratio", title="Percentage of Remote Jobs")
        Remote_Jobs.show()
        loadAnimation()
    elif menuSelection == "8":
        clearScreen()
        PartTime_FullTime = px.pie(df, names="employment_type", title="Job Types (Part-Time, Full-Time, Contract and Freelance)")
        PartTime_FullTime.show()
        loadAnimation()

    # User Defined Graphs
    elif menuSelection == "9":
        clearScreen()
        salaryRangeMax = int(input("Enter the top of the Salary Range(USD)\n: "))
        salaryRangeMin = int(input("Enter the bottom of the Salary Range(USD)\n: "))
        dfFiltered = df[(df["salary_in_usd"] >= salaryRangeMin) & (df["salary_in_usd"] <= salaryRangeMax)]
        AvgSal_SalaryRange = dfFiltered.groupby('job_title')['salary_in_usd'].mean().reset_index()
        AvgSal_SalaryRange['salary_in_usd'] = AvgSal_SalaryRange['salary_in_usd'].round(2)
        SalaryRange = px.bar(AvgSal_SalaryRange, x="job_title", y="salary_in_usd", title="Average Salary for Jobs within a user defined salary range")
        SalaryRange.show()
        loadAnimation()
    elif menuSelection == "10":
        clearScreen()
        experienceDisplay()
        expLevel = input("Enter the shortened Experience Level\n: ")
        while expLevel not in experienceList:
            clearScreen()
            experienceDisplay()
            expLevel = input("Invalid Option, Enter the shortened Experience Level\n: ")
        dfFiltered = df[df["experience_level"] == expLevel]
        AvgSal_ExpLevel = dfFiltered.groupby('job_title')['salary_in_usd'].mean().reset_index()
        AvgSal_ExpLevel['salary_in_usd'] = AvgSal_ExpLevel['salary_in_usd'].round(2)
        ExpRange = px.bar(AvgSal_ExpLevel, x="job_title", y="salary_in_usd", title="Average Salary for Jobs of a User Defined Experience Level")
        ExpRange.show()
        loadAnimation()
    elif menuSelection == "11":
        clearScreen()
        countryList()
        countryRaw = input("Enter the country you want to display\n: ")
        while countryRaw not in countryDictionary.keys():
            print("Invalid option,")
            countryRaw = input("Enter the country you want to display\n: ")
        country = country_ISO_Convert(countryRaw)
        dfFiltered = df[df["employee_residence"] == country]
        AvgSal_Country = dfFiltered.groupby('job_title')['salary_in_usd'].mean().reset_index()
        AvgSal_Country['salary_in_usd'] = AvgSal_Country['salary_in_usd'].round(2)
        Country = px.bar(AvgSal_Country, x="job_title", y="salary_in_usd", title="Average Salary for Jobs within a user defined country")
        Country.show()
        loadAnimation()
    elif menuSelection == "12":
        clearScreen()
        print("S) less than 50 employees, M) 50-250 employees, L) more than 250 employees")
        companySize = input("Enter the company size you want to display\n: ").upper()
        while companySize != "S" and companySize != "M" and companySize != "L":
            clearScreen()
            print("S) less than 50 employees, M) 50-250 employees, L) more than 250 employees")
            print("Invalid Option,")
            companySize = input("Enter the company size you want to display\n: ").upper()
        dfFiltered = df[df["company_size"] == companySize]
        AvgSal_CompanySize = dfFiltered.groupby('job_title')['salary_in_usd'].mean().reset_index()
        AvgSal_CompanySize['salary_in_usd'] = AvgSal_CompanySize['salary_in_usd'].round(2)
        CompanySize = px.bar(AvgSal_CompanySize, x="job_title", y="salary_in_usd", title="Average Salary by Job Title within a User Defined Company Size (" + companySize + ")")
        CompanySize.show()
        loadAnimation()
    elif menuSelection == "back":
        clearScreen()
        print("Returning to menu")
    else:
        clearScreen()
        print("Invalid selection")
        time.sleep(1)
    return

def dataInterprit_nG(menuSelection, df):
    if menuSelection == "1":
        clearScreen()
        startIndex_global = 0
        jobListDisplay_result = "more"
        while jobListDisplay_result == "more":
            startIndex_global = startIndex_global + 5
            jobListDisplay_result, startIndex_global = jobsListDisplay(5, startIndex_global)
        jobTitle = jobListDisplay_result
        meanSalarybyTitle = df[df['job_title'] == jobTitle]['salary_in_usd'].mean()
        meanSalarybyTitle = round(meanSalarybyTitle, 2)
        print("The mean salary for the job title, " + str(jobTitle) + ", is $" + str(meanSalarybyTitle))
        pause()
        
    elif menuSelection == "2":
        clearScreen()
        countryList() # Countries list
        country = input("Enter the Exact Country: ")
        country_3166 = country_ISO_Convert(country)
        meanSalarybyCountry = df[df['company_location'] == country_3166]['salary_in_usd'].mean()
        meanSalarybyCountry = round(meanSalarybyCountry, 2)
        print("The mean salary (converted to USD) in " + str(country) + " is $" + str(meanSalarybyCountry))
        pause()
        
    elif menuSelection == "3":
        clearScreen()
        experienceDisplay()
        experienceLevel = input("Enter Experience Level(Shortened and in CAPS): ")
        while experienceLevel not in experienceList:
            clearScreen()
            experienceDisplay()
            experienceLevel = input("Invalid Input, Enter Experience Level(Shortened and in CAPS): ")
        meanSalarybyEL = df[df['experience_level'] == experienceLevel]['salary_in_usd'].mean()
        meanSalarybyEL = round(meanSalarybyEL, 2)
        print("The mean salary for the Experience Level, " + str(experienceLevel) + ", in USD is $" + str(meanSalarybyEL))
        pause()
        
    elif menuSelection == "4":
        clearScreen()
        for year in range (2020,2026):
            meanSalarybyYear = df[df['work_year'] == year]['salary_in_usd'].mean()
            meanSalarybyYear = round(meanSalarybyYear, 2)
            print("The mean salary for the year, " + str(year) + ", was $" + str(meanSalarybyYear) +"\n")
        pause()
        
    elif menuSelection == "5":
        clearScreen()
        modeJob = df['job_title'].mode()
        print("The Mode of Job Titles (Most Common) is " + str(modeJob[0]))
        pause()
        
    elif menuSelection == "6":
        clearScreen()
        experienceDisplay()
        modeExperienceLevel = df['experience_level'].mode()
        print("The Mode of Experience Level (Most Common) is " + str(modeExperienceLevel[0]))
        pause()
        
    elif menuSelection == "7":
        clearScreen()
        modeLocationofCountry = df['company_location'].mode()
        print("The Most common (mode) location for a Company is " + str(modeLocationofCountry[0]))
        pause()
        
    elif menuSelection == "8":
        clearScreen()
        modeEmployeeResidence = df['employee_residence'].mode()[0]
        fullCountryName = [key for key, value in countryDictionary.items() if value == modeEmployeeResidence]
        if fullCountryName:
            print("The most common (mode) country of employee residence is " + str(fullCountryName))
        else:
            print("The most common (mode) country of employee residence is " + str(modeEmployeeResidence[0]))
        pause()
        
    elif menuSelection == "9":
        clearScreen()
        startIndex_global = 0
        jobListDisplay_result = "more"
        while jobListDisplay_result == "more":
            startIndex_global = startIndex_global + 5
            jobListDisplay_result, startIndex_global = jobsListDisplay(5, startIndex_global)
        jobTitle = jobListDisplay_result
        medianSalarybyTitle = df[df['job_title'] == jobTitle]['salary_in_usd'].median()
        medianSalarybyTitle = round(medianSalarybyTitle, 2)
        print("The median salary for the job title, " + str(jobTitle) + ", is $" + str(medianSalarybyTitle))
        pause()
        
    elif menuSelection == "10":
        clearScreen()
        countryList() # Countries list
        country = input("Enter the Exact Country: ")
        country_3166 = country_ISO_Convert(country)
        medianSalarybyCountry = df[df['company_location'] == country_3166]['salary_in_usd'].median()
        medianSalarybyCountry = round(medianSalarybyCountry, 2)
        print("The median salary (converted to USD) in " + str(country) + " is $" + str(medianSalarybyCountry))
        pause()
        
    elif menuSelection == "11":
        clearScreen()
        print("EN) Entry-level / Junior\nMI) Mid-level / Intermediate\nSE) Senior-level / Expert\nEX) Executive-level / Director") # Experience list
        experienceLevel = input("Enter Experience Level: ")
        medianSalarybyEL = df[df['experience_level'] == experienceLevel]['salary_in_usd'].median()
        medianSalarybyEL = round(medianSalarybyEL, 2)
        print("The median salary for the Experience Level, " + str(experienceLevel) + ", in USD is $" + str(medianSalarybyEL))
        pause()
        
    elif menuSelection == "12":
        clearScreen()
        for year in range (2020,2026):
            medianSalarybyYear = df[df['work_year'] == year]['salary_in_usd'].median()
            medianSalarybyYear = round(medianSalarybyYear, 2)
            print("The median salary for the year, " + str(year) + ", was $" + str(medianSalarybyYear) +"\n")
        pause()
        
    elif menuSelection == "13":
        clearScreen()
        salaryRange = (df['salary_in_usd'].max() - df['salary_in_usd'].min()).round(2)
        print("The range from lowest paying job and highest paying job is $" + str(salaryRange))
        print("The Highest paying salary was $" + str(df['salary_in_usd'].max()) + " and the lowest paying salary was $" + str(df['salary_in_usd'].min()))
        pause()
        
    elif menuSelection == "14":
        clearScreen()
        countryList() # Countries list
        country = input("Enter the Exact Country: ")
        country_3166 = country_ISO_Convert(country)
        dfFiltered_country = df[df['company_location'] == country_3166]
        # Checks if dataframe has any matching jobs
        if not dfFiltered_country.empty:
            country_salaryRange = (dfFiltered_country['salary_in_usd'].max() - dfFiltered_country['salary_in_usd'].min()).round(2)
            clearScreen()
            print("The range from lowest to highest paying salary in "+ str(country) +" is $" + str(country_salaryRange) + "\nThe Highest paying salary is $" + str(dfFiltered_country['salary_in_usd'].max()) + " and the lowest paying salary is $" + str(dfFiltered_country['salary_in_usd'].min()))
        else:
            clearScreen()
            print("No jobs found for" + jobTitle)
        pause()
        
    elif menuSelection == "15":
        clearScreen()
        startIndex_global = 0
        jobListDisplay_result = "more"
        while jobListDisplay_result == "more":
            startIndex_global = startIndex_global + 5
            jobListDisplay_result, startIndex_global = jobsListDisplay(5, startIndex_global)
        jobTitle = jobListDisplay_result
        dfFiltered_job = df[df['job_title'] == jobTitle]
        # Checks if dataframe has any matching jobs
        if not dfFiltered_job.empty:
            job_salaryRange = (dfFiltered_job['salary_in_usd'].max() - dfFiltered_job['salary_in_usd'].min()).round(2)
            clearScreen()
            print("The range from lowest to highest paying salary for the job title, "+ str(jobTitle)+ " is $"+ str(job_salaryRange) + "\nThe Highest paying job is $" + str((dfFiltered_job['salary_in_usd'].max())) + " and the lowest paying job is $" + str(dfFiltered_job['salary_in_usd'].min()))
        else:
            print("No jobs found for" + jobTitle)
        pause()
        
    elif menuSelection == "16":
        clearScreen()
        print("EN) Entry-level / Junior\nMI) Mid-level / Intermediate\nSE) Senior-level / Expert\nEX) Executive-level / Director") # Experience list
        experienceLevel = input("Enter Experience Level: ")
        dfFiltered_EL = df[df['experience_level'] == experienceLevel]
        # Checks if dataframe has any matching experience levels
        if not dfFiltered_EL.empty:
            EL_salaryRange = (dfFiltered_EL['salary_in_usd'].max() - dfFiltered_EL['salary_in_usd'].min()).round(2)
            clearScreen()
            print("The range from lowest to highest paying salary for the Experience Level, "+ str(experienceLevel)+ " is $"+ str(EL_salaryRange) + "\nThe Highest paying salary was $" + str(dfFiltered_EL['salary_in_usd'].max()) + "and the Lowest paying salary was $" + str(dfFiltered_EL['salary_in_usd'].min()))
        else:
            print("No jobs found for" + jobTitle)
        pause()
        
    elif menuSelection == "back":
        clearScreen()
        print("Returning to menu")
        
    else:
        clearScreen()
        print("Invalid selection")
        time.sleep(1)

"""
# Tool used to make lists of unique entries for user inputs

# I only need all unique job titles, company countries and experience
df = pd.read_csv('salaries_cleaned.csv') # load the dataframe locally

#get unique values
jobTitles_Unique = df['job_title'].unique()
companyCountries_Unique = df['company_location'].unique()
experienceLevel_unique = df['experience_level'].unique()

jobTitles = open('pandasUnique.txt','w') # open to overwrite old data
# write the data
jobTitles.write("Pandas Unique Data, used to make lists for user inputs\n\n")
jobTitles.write("Job Titles\n\n" + str(jobTitles_Unique))
jobTitles.write("\n\nCompany Locations\n\n" + str(companyCountries_Unique))
jobTitles.write("\n\nExperience Levels\n\n" + str(experienceLevel_unique))
jobTitles.close() # save to file
"""