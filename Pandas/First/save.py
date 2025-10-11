import pandas as pd

data={
    "Name":['ABC','DEF','GHI'],
    "Age":[10,20,30],
    "City":['Bangalore','Hyedrabad','Mumbai']
}
df=pd.DataFrame(data)
print(df)

#df.to_csv("output.csv",index=False)
df.to_excel("output1.xlsx",index=False)
#df.to_json("output2.json",index=False)