import pandas as pd
data={
    "Name":["Abc","Ghi",'Def',"Jkl","Pqr",'Vwx','Yza',"Mno",'Eiou','Stu'],
    "Age":[10,20,60,61,65,30,70,50,40,65],
    "Salary":[10000,20000,30000,40000,50000,60000,61000,65000,70000,65000],
 #   "Perfomance Score":[50,54,59,85,79,64,89,55,32,58]

}
df=pd.DataFrame(data)
print(df)

print(df["Salary"].mean())
print()