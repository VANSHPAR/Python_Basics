import pandas as pd

data={
    "Name":["Abc",None,"Ghi","Jkl","Mno","Pqr",'Stu','Vwx','Yza','Eiou'],
    "Age":[10,None,30,40,50,60,61,65,70,65],
    "Salary":[10000,None,30000,40000,50000,60000,61000,65000,70000,65000],
    "Perfomance Score":[50,None,59,85,79,64,89,55,32,58]

}
df=pd.DataFrame(data)
print(df)

#df.fillna(0,inplace=True)
#Fill value with median value
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
df['Perfomance Score'].fillna(df['Perfomance Score'].mean(),inplace=True)

print(df)