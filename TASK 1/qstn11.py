import pandas as pd
diamonds = pd.read_csv('C:\\Users\\hp\\Desktop\\diamonds.csv')
print("Original Dataframe:")
print(diamonds.shape)
print("\nDuplicate rows of diamonds DataFrame:")
print(diamonds.duplicated(). sum())                      
   
    


