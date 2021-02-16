#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: 
#Group Name: <...>
#Class: 
#Date: <...>
#Version: <...>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):
  past10 = df.iloc[-121:480]

  #print number of rows in dataframe
  print("There are " + str(len(past10)) + " data rows read. \n")

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows for the last 10 years: \n")
  print(past10)
  top3summed = past10.drop('Year', axis=1).sum(numeric_only=True,axis=0)
  top3summed = top3summed.sort_values(ascending = False)
  print("Top 3 Countries that have visited Singapore in the past 10 years")
  print("Country Name | Total Visitors")
  print(top3summed[0:3])

  #display a specific country (Australia) in column #33
  country_label = past10.columns[33]
  print("\n\n" + country_label + "was selected.")

  #display a sorted dataframe based on selected country
  print(" The" + country_label + "was sorted in ascending order. \n")
  sorted_df =past10.sort_values(country_label,ascending=[0])
  print(sorted_df)

  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################