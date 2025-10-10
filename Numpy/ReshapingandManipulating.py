import numpy as np

#Reshaping ->it doesn't return copy it returns view 
print("------Reshaping of array-------")
arr=np.array([1,2,3,5,7,9])
new_arr=arr.reshape(3,2)
print(new_arr)
arr1=arr.reshape(6,1)
print(arr1)

#Flattning array ->convert multidimensonal array into 1d array
#ravel() ->returns view
#flatten() -> return copy
print("------Flattening of array-------")
arr3=np.array([[[1,2],[3,4],[5,6],[7,8]]])
print("ravel",arr3.ravel())
print("flatten",arr3.flatten())