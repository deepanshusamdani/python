# program to apply the conition on the fields to take only those rows which follow the logic

import pandas as pd

#taking records
record = { 
  'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ], 
  'Age': [21, 19, 20, 18, 17, 21], 
  'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'], 
  'Percentage': [88, 92, 95, 70, 65, 78]} 
  
# create a dataframe 
dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage']) 

#I want to apply the multiple condintion on the "Percentage" field and select only those rows
#  converting the datatype of Percentage from 'int' to str
dataframe['Percentage'] = dataframe['Percentage'].apply(str)

#creating the list for the multiple values
selection = ['88', '95']

#it will return only those rows where the percentage has those values
dataframe.loc[dataframe['Percentage'].isin(selection)]

