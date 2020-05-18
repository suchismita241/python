import pandas as pd
diamonds = pd.read_csv('C:\\Users\\hp\\Desktop\\diamonds.csv')
print("Original Dataframe:")
print(diamonds.head())
print("Number of rows and columns:")
print(diamonds.shape)
print("After droping those rows where values are missing:")
print(diamonds.dropna(how='any').shape)                      
   
    


