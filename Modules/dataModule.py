# .csv file cleaner module

# Removes all rows with missing values, all duplicated and rows with NULL values
# then writes to fileName_cleaned.csv

#dependant modules
import pandas as pd
import time as t

#file cleaner function, drops all rows with missing values, all duplicated rows and rows with NULL values
def fileClean():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    originalPath = input("Enter the name of the file you want to clean (Leave spaces out of the file name, type .csv at the end)\n:")
    #checks if path contains .csv at the end
    if originalPath[-4:] != ".csv":
        print("Enter a file containing '.csv'")
        t.sleep(2)
        return
    #opens file as a dataframe
    df = pd.read_csv(originalPath)
    
    #prints a sample of the dataframe
    print(df.sample(10))
    rightFileConfirm = input("Is this the correct file? (Check columns, tables, etc.)(y/N)\n:").lower()
    
    #file isnt correct
    if rightFileConfirm == "n":
        print("Restarting...")
        t.sleep(2)
        return "failed", ""
    
    #file correct
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
    
    #invalid input, how did you get here?
    else:
        print("Invalid input\nRestarting...")
        t.sleep(2)
        return "failed", ""