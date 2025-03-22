# .csv file cleaner module

# Removes all rows with missing values, all duplicated and rows with NULL values
# then writes to fileName_cleaned.csv

#modules
import pandas as pd

def fileClean():
    originalPath = input("Enter the name of the file you want to clean (Leave spaces out of the file name, type .csv at the end)\n:")
    if originalPath[-4:] != ".csv":
        print("Enter a file containing '.csv'")
        return
    df = pd.read_csv(originalPath)
    print(df.sample(10))

    rightFileConfirm = input("Is this the correct file? (y/n)\n:")
    if rightFileConfirm == "n":
        print("Please re-run the program and enter the correct file name")
        exit()
    elif rightFileConfirm == "y":
        print("Cleaning file...")
        df = df.dropna()
        df = df.drop_duplicates()
        if 'salary ' in df.columns:
            df = df[df['salary'] <= 400000]
        
        cleanedPath = (originalPath[:-4] + "_cleaned.csv")
        df.to_csv(cleanedPath, index=False)
        print("File cleaned and saved as " + cleanedPath)