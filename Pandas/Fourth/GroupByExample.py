import pandas as pd
data={
    "Name":["Abc","Ghi",'Def',"Jkl","Pqr"],
    "Age":[10,20,60,61,20],
    "Salary":[30000,40000,50000,45000,38000]
 #   "Perfomance Score":[50,54,59,85,79,64,89,55,32,58]

}

#For single column
# df=pd.DataFrame(data)
# grouped=df.groupby("Age")["Salary"].sum()
# print(grouped)

#For muliple cols
df=pd.DataFrame(data)
grouped=df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)

#Agregation functions
#sum()  mean()  count()counts nan values
#min() max() std()
