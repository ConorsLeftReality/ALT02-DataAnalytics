#dependancies
import pandas as pd
import plotly.express as px
import time
import os

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
# Made by pandasUnique code at the bottom :)
jobTitles_list = [
    'Customer Success Manager', 'Engineer', 'Applied Scientist', 'Data Analyst', 
    'Software Development Engineer', 'Research Scientist', 'Data Scientist', 
    'Platform Engineer', 'Computational Biologist', 'AI Data Scientist', 
    'Admin & Data Analyst', 'Cloud Engineer', 'Data Management Specialist', 
    'Data Product Owner', 'Software Engineer', 'Machine Learning Engineer', 
    'Associate', 'Data Engineer', 'Product Manager', 'Data Operations Engineer', 
    'Business Intelligence Engineer', 'Research Engineer', 'Analytics Engineer', 
    'Analyst', 'Actuarial Analyst', 'Manager', 'Architect', 'Software Developer', 
    'Member of Technical Staff', 'BI Analyst', 'AI Engineer', 
    'Data Governance Analyst', 'Developer', 'DevOps Engineer', 
    'Business Intelligence Analyst', 'Site Reliability Engineer', 
    'Computational Scientist', 'Data Management Analyst', 
    'Data and Reporting Analyst', 'Solution Architect', 'Data Reporting Analyst', 
    'Data Architect', 'Solutions Architect', 'Data Manager', 'Data Reporter', 
    'Data Governance', 'Business Intelligence Developer', 'Solutions Engineer', 
    'Database Administrator', 'Consultant', 'Product Analyst', 'Data Specialist', 
    'Quantitative Developer', 'Research Assistant', 'BI Developer', 
    'Quantitative Researcher', 'Product Designer', 'Machine Learning Scientist', 
    'Research Associate', 'Product Owner', 'Insight Analyst', 'Statistician', 
    'Engineering Manager', 'Data Analytics Manager', 'Data Modeler', 
    'Systems Engineer', 'Data Platform Engineer', 'Technical Lead', 
    'Bioinformatician', 'AI Researcher', 'Data Developer', 
    'Quantitative Analyst', 'Head of AI', 'Lead Engineer', 'Prompt Engineer', 
    'Data Visualization Analyst', 'Python Developer', 'Analytics Specialist', 
    'Full Stack Developer', 'Head of Data', 'AI Governance Lead', 
    'Director of Machine Learning', 'AI Architect', 'Enterprise Account Executive', 
    'Backend Engineer', 'DataOps Engineer', 'Data Governance Specialist', 
    'System Engineer', 'Data Visualization Engineer', 'AI Developer', 
    'Data Governance Lead', 'Business Analyst', 'Tableau Developer', 
    'Computer Vision Engineer', 'Account Executive', 'Product Specialist', 
    'Data Governance Manager', 'Business Intelligence', 'Data Operations', 
    'Data Strategist', 'Data Quality Specialist', 'Data and Reporting Professional', 
    'Robotics Engineer', 'Cloud Database Engineer', 'Data Integration Engineer', 
    'Principal Researcher', 'Research Analyst', 'AI Data Engineer', 
    'ETL Developer', 'Bioinformatics Scientist', 'Full Stack Engineer', 
    'Postdoctoral Fellow', 'Technology Integrator', 'Algorithm Developer', 
    'AI Specialist', 'Data Integrator', 'Data Lead', 
    'Business Intelligence Specialist', 'Encounter Data Management Professional', 
    'Java Developer', 'Power BI Developer', 'AI Product Owner', 
    'Principal Software Architect', 'Statistical Programmer', 
    'Data Operations Specialist', 'Master Data Management', 
    'Data Analytics Specialist', 'MLOps Engineer', 'Data Product Manager', 
    'Security Researcher', 'AI Research Scientist', 'Data Operations Analyst', 
    'Principal Statistical Programmer', 'Data Team Lead', 
    'Data Infrastructure Engineer', 'Big Data Developer', 'BI Engineer', 
    'Developer Advocate', 'Postdoctoral Researcher', 'Tech Lead', 
    'Data Visualization Specialist', 'Scala Spark Developer', 
    'Sales Development Representative', 'Machine Learning Researcher', 
    'Power BI', 'AI Scientist', 'Staff Data Scientist', 'Application Developer', 
    'Decision Scientist', 'Cloud Database Administrator', 
    'AI Machine Learning Engineer', 'Data Integrity Specialist', 
    'Power BI Specialist', 'Analytics Lead', 'GenAI Architect', 
    'Lead Data Analysis', 'Data Management Associate', 'Data Integration Specialist', 
    'Lead Analyst', 'Head of Machine Learning', 'Data Management Lead', 
    'QA Engineer', 'Data Analytics Consultant', 'Data Quality Analyst', 
    'Data Visualization Developer', 'Software Architect', 'Machine Learning Developer', 
    'Data Strategy Lead', 'Data Scientist Associate', 'Data Quality Lead', 
    'Data Analytics Lead', 'Business Intelligence Manager', 'Risk Analyst', 
    'Marketing Science Partner', 'Data Reporting Specialist', 
    'Clinical Data Operator', 'AI Lead', 'Machine Learning Specialist', 
    'Research Data Manager', 'Technical Specialist', 'Applied Research Scientist', 
    'Lead Data Management', 'Data Analytics Developer', 'Machine Learning Architect', 
    'Machine Learning Lead', 'Stage', 'Technical Writer', 
    'Data Quality Engineer', 'Data Integration Analyst', 
    'Safety Data Management Specialist', 'Business Intelligence Lead', 
    'Data Operations Manager', 'Big Data Analyst', 'Data Scientist Manager', 
    'Pricing Analyst', 'Lead Data Engineer', 'AI Engineering Manager', 
    'Backend Developer', 'Data Management Coordinator', 'Analytics Analyst', 
    'Controls Engineer', 'Machine Learning Tech Lead', 
    'Business Development Manager', 'Data Management Consultant', 
    'Business Insights Manager', 'Power BI Administrator', 
    'Data Integration Developer', 'Data Integrity Analyst', 
    'Platform Data Engineer', 'Bear Robotics', 
    'Principal Application Delivery Consultant', 'Chatbot Developer', 
    'Artificial Intelligence Engineer', 'Data Governance Architect', 
    'Power BI Consultant', 'Backend Software Engineer', 'AI Product Manager', 
    'Data Operations Associate', 'ML Infrastructure Engineer', 
    'Cloud Developer', 'Data Operations Lead', 'Fullstack Engineer', 
    'Machine Learning Quality Engineer', 'Security Engineer', 
    'Databricks Engineer', 'Infrastructure Engineer', 'Solution Engineer', 
    'Big Data Engineer', 'Machine Learning Performance Engineer', 
    'Data Analytics Associate', 'Power BI Architect', 
    'Machine Learning Platform Engineer', 'AI Solution Architect', 
    'Data Scientist Lead', 'Machine Vision Engineer', 
    'Data Governance Engineer', 'Machine Learning Model Engineer', 
    'Marketing Analyst', 'Data Management Manager', 
    'Marketing Analytics Manager', 'Applied AI ML Lead', 
    'Data Strategy Manager', 'Machine Learning Manager', 'Data Product Analyst', 
    'Data Quality Manager', 'Elasticsearch Administrator', 
    'Machine Learning Infrastructure Engineer', 'People Data Analyst', 
    'Frontend Engineer', 'NLP Engineer', 'SAS Developer', 
    'Data Analytics Team Lead', 'Machine Learning Modeler', 
    'Data Integration Coordinator', 'AI Programmer', 
    'Head of Business Intelligence', 'ETL Engineer', 'AI Research Engineer', 
    'Business Intelligence Consultant', 'Robotics Software Engineer', 
    'AI Software Engineer', 'Lead AI Engineer', 'AI Software Development Engineer', 
    'Master Data Specialist', 'Consultant Data Engineer', 'Manager Data Management', 
    'Director of Business Intelligence', 'Lead Data Scientist', 
    'CRM Data Analyst', 'BI Data Analyst', 'Applied Data Scientist', 
    'Data DevOps Engineer', 'Quantitative Research Analyst', 
    'Lead Machine Learning Engineer', 'Machine Learning Research Engineer', 
    'Data Analyst Lead', 'Data Pipeline Engineer', 'Lead Data Analyst', 
    'Business Data Analyst', 'Marketing Data Scientist', 
    'Deep Learning Engineer', 'Financial Data Analyst', 'Azure Data Engineer', 
    'Principal Data Scientist', 'Staff Data Analyst', 
    'Machine Learning Software Engineer', 'Applied Machine Learning Scientist', 
    'Principal Machine Learning Engineer', 'Principal Data Engineer', 
    'Staff Machine Learning Engineer', 'Business Intelligence Data Analyst', 
    'Finance Data Analyst', 'Software Data Engineer', 'Compliance Data Analyst', 
    'Cloud Data Engineer', 'Analytics Engineering Manager', 
    'AWS Data Architect', 'Product Data Analyst', 
    'Autonomous Vehicle Technician', 'Sales Data Analyst', 
    'Applied Machine Learning Engineer', 'BI Data Engineer', 
    'Deep Learning Researcher', 'Big Data Architect', 
    'Computer Vision Software Engineer', 'Marketing Data Engineer', 
    'Data Science Tech Lead', 'Marketing Data Analyst', 
    'Principal Data Architect', 'Data Analytics Engineer', 
    'Cloud Data Architect', 'Principal Data Analyst']

def clearScreen(): # declutters
    os.system('cls' if os.name == 'nt' else 'clear')

def countryList():
    print("Netherlands, United States\nUnited Kingdom, Lithuania\nCanada, Spain\nGermany, Latvia\nBelgium, France\nSlovakia, Philippines\nIreland, Australia\nBrazil, India")
    print("Poland, Peru\nArgentina, Austria\nSwitzerland, New Zealand\nPortugal, Serbia\nFinland, Taiwan\nNorway, Ukraine\nEl Salvador, Ecuador\nChile, Dominican Republic")
    print("Mexico, Colombia\nMalta, Denmark\nIndonesia, Malaysia\nKosovo, Costa Rica\nJapan, Zambia\nPuerto Rico, Armenia\nSingapore, Luxembourg\nItaly, Cyprus")
    print("Congo (Democratic Republic), Israel\nCzech Republic, South Korea\nSouth Africa, Egypt\nLebanon, Greece\nNigeria, Bulgaria\nHungary, Croatia\nKenya, Sweden")
    print("Turkey, Pakistan\nHonduras, Romania\nVenezuela, Algerian\nAmerican Samoa, United Arab Emirates\nSaudi Arabia, Oman\nBosnia and Herzegovina, Estonia")
    print("Vietnam, Gibraltar\nSlovenia, Mauritius\nRussia, Qatar\nGhana, Andorra\nHong Kong, Central African Republic\nThailand, Iran\nBahamas, Iraq\nChina, Moldova")
    return

def experienceDisplay():
    print("EN. Entry-level / Junior\nMI.  Mid-level / Intermediate\nSE. Senior-level / Expert\nEX. Executive-level / Director")

experienceList = ['EN','MI','SE','EX'] # list to verify off of

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
        result = input("Enter exact Job title, or 'more' for 5 more titles: ")
    return result,(startIndex + batchSize) # receiving side of code will call this the new startIndex

# data interpret side of job list function
#
#jobListDisplay_result = "more"
#        while jobListDisplay_result == "more":
#            jobListDisplay_result, startIndex = jobsListDisplay(5, startIndex)
#        jobTitle = jobListDisplay_result

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
        if 'salary_in_usd ' in df.columns:
            df = df[df['salary_in_usd'] <= 400000] # salary doesnt go over 400k (i mean its possible but i dont want to get bad data)
            df = df[df['salary_in_usd'] > 5000] # salary is over 5000 euro (we dont like child labour or negative salaries)
        #making cleaned path
        cleanedPath = (originalPath[:-4] + "_cleaned.csv")
        df.to_csv(cleanedPath, index=False)
        print("File cleaned and saved as " + cleanedPath)
        return "success", cleanedPath

#################################################################################################################################################################

def dataInterprit_G(menuSelection, df):
    if menuSelection == "1":
        clearScreen()
        AvgSal_TitleGrouping = df.groupby('job_title')['salary_in_usd'].mean().reset_index()
        AvgSal_Title = px.bar(AvgSal_TitleGrouping, x="job_title", y="salary_in_usd", title="Average Salary by Job Title")
        AvgSal_Title.show()
        loadAnimation()
    elif menuSelection == "2":
        clearScreen()
        AvgSal_CountryGrouping = df.groupby('company_location')['salary_in_usd'].mean().reset_index()
        AvgSal_Country = px.bar(AvgSal_CountryGrouping, x="company_location", y="salary_in_usd", title="Average Salary by Business Country (ISO 3166 Format)")
        AvgSal_Country.show()
        loadAnimation()
    elif menuSelection == "3":
        clearScreen()
        AvgSal_ExpGrouping = df.groupby('experience_level')['salary_in_usd'].mean().reset_index()
        AvgSal_Exp = px.bar(AvgSal_ExpGrouping, x="experience_level", y="salary_in_usd", title="Average Salary by Experience")
        AvgSal_Exp.show()
        loadAnimation()
    elif menuSelection == "4":
        clearScreen()
        AvgSal_TimeGrouping = df.groupby('work_year')['salary_in_usd'].mean().reset_index()
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
        Pay_highToLow = px.pie(dfFiltered, names="job_title", values="salary_in_usd", title="Top Highest and Lowest Paying Jobs")
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
        salaryRangeMax = input("Enter the top of the Salary Range(USD)\n: ")
        salaryRangeMin = input("Enter the bottom of the Salary Range(USD)\n: ")
        dfFiltered = df[(df["salary_in_usd"] >= salaryRangeMin) & (df["salary_in_usd"] <= salaryRangeMax)]
        SalaryRange = px.bar(dfFiltered, x="job_title", y="salary_in_usd", title="Jobs within a user defined salary range")
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
        CompanySize = px.bar(AvgSal_CompanySize, x="job_title", y="salary_in_usd", title="Average Salary by Job Title within a User Defined Company Size (" + companySize + ")")
        CompanySize.show()
        loadAnimation()
    elif menuSelection == "exit":
        clearScreen()
        exitProgram = True
        print("Exiting program, thank you for using the Data Display Program!")
        exit()
    else:
        clearScreen()
        print("Invalid selection")
        time.sleep(1)
    return

def dataInterprit_nG(menuSelection, df):
    if menuSelection == "1":
        startIndex_global = 0
        jobListDisplay_result = "more"
        while jobListDisplay_result == "more":
            startIndex_global = startIndex_global + 5
            jobListDisplay_result, startIndex_global = jobsListDisplay(5, startIndex_global)
        jobTitle = jobListDisplay_result
        meanSalarybyTitle = df[df['job_title'] == jobTitle]['salary_in_usd'].mean()
        print("The mean salary for the job title, " + str(jobTitle) + ", is $" + str(meanSalarybyTitle))
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "2":
        countryList() # Countries list
        country = input("Enter the Exact Country: ")
        country_3166 = country_ISO_Convert(country)
        meanSalarybyCountry = df[df['company_location'] == country_3166]['salary_in_usd'].mean()
        print("The mean salary (converted to USD) in " + str(country) + " is $" + str(meanSalarybyCountry))
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "3":
         # Experience list
        experienceLevel = input("Enter Experience Level(Shortened and in CAPS): ")
        meanSalarybyEL = df[df['experience_level'] == experienceLevel]['salary_in_usd'].mean()
        print("The mean salary for the Experience Level, " + str(experienceLevel) + ", in USD is $" + str(meanSalarybyEL))
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "4":
        for year in range (2020,2026):
            meanSalarybyYear = df[df['work_year'] == year]['salary_in_usd'].mean()
            print("The mean salary for the year, " + str(year) + ", was $" + str(meanSalarybyYear) +"\n")
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "5":
        modeJob = df['job_title'].mode()
        print("The Mode of Job Titles (Most Common) is " + str(modeJob))
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "6":
        modeExperienceLevel = df['experience_level'].mode()
        print("The Mode of Experience Level (Most Common) is " + str(modeExperienceLevel))
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "7":
        modeLocationofCountry = df['company_location'].mode()
        print("The Most common (mode) location for a Company is " + str(modeLocationofCountry))
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "8":
        modeEmployeeResidence = df['employee_residence'].mode()
        print("The most common (mode) country of employee residence is " + str(modeEmployeeResidence))
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "9":
        startIndex_global = 0
        jobListDisplay_result = "more"
        while jobListDisplay_result == "more":
            startIndex_global = startIndex_global + 5
            jobListDisplay_result, startIndex_global = jobsListDisplay(5, startIndex_global)
        jobTitle = jobListDisplay_result
        medianSalarybyTitle = df[df['job_title'] == jobTitle]['salary_in_usd'].median()
        print("The median salary for the job title, " + str(jobTitle) + ", is $" + str(medianSalarybyTitle))
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "10":
        countryList() # Countries list
        country = input("Enter the Exact Country: ")
        country_3166 = country_ISO_Convert(country)
        medianSalarybyCountry = df[df['company_location'] == country_3166]['salary_in_usd'].median()
        print("The median salary (converted to USD) in " + str(country) + " is $" + str(medianSalarybyCountry))
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "11":
        print("EN) Entry-level / Junior\nMI) Mid-level / Intermediate\nSE) Senior-level / Expert\nEX) Executive-level / Director") # Experience list
        experienceLevel = input("Enter Experience Level: ")
        medianSalarybyEL = df[df['experience_level'] == experienceLevel]['salary_in_usd'].median()
        print("The median salary for the Experience Level, " + str(experienceLevel) + ", in USD is $" + str(medianSalarybyEL))
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "12":
        for year in range (2020,2026):
            medianSalarybyYear = df[df['work_year'] == year]['salary_in_usd'].median()
            print("The median salary for the year, " + str(year) + ", was $" + str(medianSalarybyYear) +"\n")
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "13":
        salaryRange = df['salary_in_usd'].max() - df['salary_in_usd'].min()
        print("The range from lowest paying job and highest paying job is $" + str(salaryRange))
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "14":
        countryList() # Countries list
        country = input("Enter the Exact Country: ")
        country_3166 = country_ISO_Convert(country)
        dfFiltered_country = df[df['company_location'] == country_3166]
        # Checks if dataframe has any matching jobs
        if not dfFiltered_country.empty:
            country_salaryRange = dfFiltered_country['salary_in_usd'].max() - dfFiltered_country['salary_in_usd'].min()
            print("The range from lowest to highest paying salary in "+ str(country) +" is $" + str(country_salaryRange))
        else:
            print("No jobs found for" + jobTitle)
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "15":
        startIndex_global = 0
        jobListDisplay_result = "more"
        while jobListDisplay_result == "more":
            startIndex_global = startIndex_global + 5
            jobListDisplay_result, startIndex_global = jobsListDisplay(5, startIndex_global)
        jobTitle = jobListDisplay_result
        dfFiltered_job = df[df['job_title'] == jobTitle]
        # Checks if dataframe has any matching jobs
        if not dfFiltered_job.empty:
            job_salaryRange = dfFiltered_job['salary_in_usd'].max() - dfFiltered_job['salary_in_usd'].min()
            print("The range from lowest to highest paying salary for the job title, "+ str(jobTitle)+ " is $"+ str(job_salaryRange))
        else:
            print("No jobs found for" + jobTitle)
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "16":
        print("EN) Entry-level / Junior\nMI) Mid-level / Intermediate\nSE) Senior-level / Expert\nEX) Executive-level / Director") # Experience list
        experienceLevel = input("Enter Experience Level: ")
        dfFiltered_EL = df[df['experience_level'] == experienceLevel]
        # Checks if dataframe has any matching experience levels
        if not dfFiltered_EL.empty:
            EL_salaryRange = dfFiltered_EL['salary_in_usd'].max() - dfFiltered_EL['salary_in_usd'].min()
            print("The range from lowest to highest paying salary for the Experience Level, "+ str(experienceLevel)+ " is $"+ str(EL_salaryRange))
        else:
            print("No jobs found for" + jobTitle)
        print("\nReturning to menu in 8 seconds...")
        time.sleep(8)
    elif menuSelection == "exit":
        exitProgram = True
        print("Exiting program, thank you for using the Data Display Program!")
        exit()
    else:
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