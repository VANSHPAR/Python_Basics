import pandas as pd

data={
    "Name":["Abc",'Def',"Ghi","Jkl","Mno","Pqr",'Stu','Vwx','Yza','Eiou'],
    "Age":[10,None,30,40,50,60,61,65,70,65],
    "Salary":[10000,None,30000,40000,50000,60000,61000,65000,70000,65000],
    "Perfomance Score":[50,None,59,85,79,64,89,55,32,58]

}
df=pd.DataFrame(data)
print(df)

df.interpolate(method="linear",axis=0,inplace=True)
#method="linear" or "polynomial" or "time"
print(df)


#Time Series data
#numeric data with trends
#avoid drooping rows

#not work with name,ids etc.
