import numpy as np

#Dot product
arr1=np.array([[1,2],[4,5]])
arr2=np.array([[2,3],[5,6]])
dot=np.dot(arr1,arr2)
print(dot)
product=arr1@arr2
print(product)


#Tranpose
print("------Tranpose------")
arr1=np.array([[1,2],[4,5]])
tra=arr1.T
print(tra)


#Trace

print("------Trace------")
arr1=np.array([[1,2],[4,5]])
print(np.trace(arr1))