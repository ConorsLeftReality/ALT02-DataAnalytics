# **ALT02 - DataAnalytics**
# **Active Learning Task for Leaving Cert, based on the python modules Pandas and Plotly, for use with .csv files**

Based on *'The AI, ML, Data Science Salary (2020- 2025)'* dataset by Samith Chimminiyan,
under the CC0: Public Domain License on Kaggle
https://www.kaggle.com/datasets/samithsachidanandan/the-global-ai-ml-data-science-salary-for-2025

# **How To Use:**
Download all the files and keep them where they are in the folders

dataInterpreter.py is the main file you run to get analytics on salaries.csv, which it will automatically clean and create salaries_cleaned.csv

This program is able to be run on Graphical and Non-Graphical Operating Systems, as plotly runs in a browser and pandas can run in the commmand line.

# **Mandatory Task Requirements:**
Your program must sucessfully read in information from your external dataset

Your data must be cleaned to make sure its in a usable format

Your program must display some statistical information about some of the data i.e. the mean, mode, median and range of some of the data (graphical and non graphical results, useful for users on non-graphical Operating Systems)

You create one graph based on your analysis of your chosen dataset (plotly)

The user can choose which part of the dataset th get statistics about (User Defined Graphs?)

The user has a choice of what type of statistics they get (menu?)

The program can present multiple graphs based on the users's choice (i am assuming at one time)

# **Non-Graphical Data to display:**

Mean:
  1. Mean salary by title
  2. Mean salary by country
  3. Mean salary by experience
  4. Mean salary over time

Mode:
  1. Mode of job title
  2. Mode of Experience
  3. Mode of Countrys worked
  4. Mode of Countries lived in (retitle these conor)
     
Median:
  1. Median salary by title
  2. Median salary by country
  3. Median salary by experience
  4. Median salary over time
     
Range:
  1. Range of Pay (Highest to lowest, while displaying the lowest and highest salary)
  2. Range of Pay by User Defined Country (Prints Country list when selected)
  3. Range of Pay by User Defined Title (Prints list)
  4. Range of Pay by User Defined Experience (Prints list)
 
# **Graphical data to display:**
  Standard Results

  1. average salary by title
  2. average salary by country
  3. average salary by experience
  4. average salary over time
  5. amount of jobs by title and country
  6. highest paying job and lowest paying job
  7. how many jobs are remote
  8. part-time vs full-time ratio

  User Defined Results

  9. statistics for jobs within a user defined salary range
  10. statistics for jobs within a user defined experience level
  11. statistics for jobs within a user defined country
  12. statistics for jobs within a user defined company size
