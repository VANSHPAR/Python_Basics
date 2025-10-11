#understand the data set
#identify the problems
#plan next step

import pandas as pd

#read data from csv into data frame
df=pd.read_csv(r"C:\Users\Vansh Parmar\OneDrive\Attachments\Desktop\min\coding\Python\Pandas\First\sales_data_sample.csv",encoding="latin1")

print('Display first 10 rows')
print(df.head(10))

print('Display last 10 rows')
print(df.tail(10))