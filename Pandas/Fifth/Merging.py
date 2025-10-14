import pandas as pd

df1=pd.DataFrame({
    "Cid":[1,2,3,4],
    "Name":["Abc","Def","Ghi","Jkl"]
})

df2=pd.DataFrame({
    "Cid":[1,2,6,5],
    "Order Amount":[150,1200,186,1999]
})

merged=pd.merge(df1,df2,on="Cid",how="inner")
#How=Inner or outer or left or rigt
print("inner join")
print(merged)

merged=pd.merge(df1,df2,on="Cid",how="outer")
#How=Inner or outer or left or rigt
print("Outer join")
print(merged)

merged=pd.merge(df1,df2,on="Cid",how="left")
#How=Inner or outer or left or rigt
print("left join")
print(merged)


merged=pd.merge(df1,df2,on="Cid",how="right")
#How=Inner or outer or left or rigt
print("right join")
print(merged)

