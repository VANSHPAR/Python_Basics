import pandas as pd

#read data from csv into data frame
#df=pd.read_csv(r"C:\Users\Vansh Parmar\OneDrive\Attachments\Desktop\min\coding\Python\Pandas\First\sales_data_sample.csv",encoding="latin1")
#df=pd.read_excel(r"C:\Users\Vansh Parmar\OneDrive\Attachments\Desktop\min\coding\Python\Pandas\First\SampleSuperstore.xlsx")
df=pd.read_json(r"C:\Users\Vansh Parmar\OneDrive\Attachments\Desktop\min\coding\Python\Pandas\First\sample_Data.json")
print(df)

#read data from cloud gcsfs