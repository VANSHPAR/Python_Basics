#cols,rows
#what type of cols
#missing data

import pandas as pd

#read data from csv into data frame
df=pd.read_csv(r"C:\Users\Vansh Parmar\OneDrive\Attachments\Desktop\min\coding\Python\Pandas\First\sales_data_sample.csv",encoding="latin1")

print("Info of dataset")
print(df.info())


data={
    "Name":['ABC','DEF','GHI'],
    "Age":[10,20,30],
    "City":['Bangalore','Hyedrabad','Mumbai']
}
df1=pd.DataFrame(data)
print('info of data')
print(df1.info())