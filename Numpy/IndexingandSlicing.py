import numpy as np
arr=np.array([1,3,5,7])
print(arr[3])
print(arr[-1],arr[-2])


#slicing
print("------slicing-------")
arr=np.array([1,2,3,4,5,6,9])
print(arr[0:2])
print(arr[:3])
print(arr[1:])
print(arr[0:5:2])
print(arr[::-1])


#Fancy Indexing
print('-------Fancy Indexing-------')
arr=np.array([1,2,3,4,5,6,9])
print(arr[[0,2,4,6]])

#Filtering -> it filters data from arr for given condition
print('-------filtering data-----')
arr=np.array([1,2,3,4,5,6,9])
print(arr[arr>2])
print(arr[arr%2!=0])