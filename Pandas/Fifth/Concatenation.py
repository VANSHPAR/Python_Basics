#Verticaly concat.. (row wise)
#Horizontally concat.. (col wise)
import pandas as pd

df1=pd.DataFrame({
    "Cid":[1,2,3,4],
    "Name":["Abc","Def","Ghi","Jkl"]
})

df2=pd.DataFrame({
    "Cid":[5,6,7,8],
    "Name":["Mno","Pqr","Stu","Vwx"]
})

#Vertically
res=pd.concat([df1,df2],axis=0,ignore_index=True)
print("Vertically Concatenated")
print(res)


#Vertically
res=pd.concat([df1,df2],axis=1,ignore_index=True)
print("Horizonatally Concatenated")
print(res)