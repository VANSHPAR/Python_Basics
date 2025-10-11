#Select specific col
#Filter rows
#Filter rows for multiple conditions

#Seletcing cols
#returs series for one col
#retuns dataframe for multiple cols

#Filtering rows
import pandas as pd

data={
    "Name":["Abc","Def","Ghi","Jkl","Mno","Pqr",'Stu','Vwx','Yza','Eiou'],
    "Age":[10,20,30,40,50,60,61,65,70,65],
    "Salary":[10000,20000,30000,40000,50000,60000,61000,65000,70000,65000],
    "Perfomance Score":[50,63,59,85,79,64,89,55,32,58]

}
df=pd.DataFrame(data)
print(df)


print("----Select Column----")
print(df["Name"])


print("----Select Multiple Columns----")
print(df[["Name","Salary"]])


