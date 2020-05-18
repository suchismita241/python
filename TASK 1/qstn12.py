import pandas as pd
diamonds = pd.read_csv('C:\\Users\\hp\\Desktop\\diamonds.csv')
print("Original Dataframe:")
print(diamonds.shape)
print("\nSample 75% of diamonds DataFrame rows without replacement:")
result = diamonds.sample(frac=0.75, random_state=98)
print(result)
print("\nRemaining 25% of the rows:")
print(diamonds.loc[~diamonds.index.isin(result.index), :])                     
   
    


