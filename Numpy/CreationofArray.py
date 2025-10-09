import  numpy as np


#using python list
arr=np.array([1,35,5])
print(arr)

#with default values
zerosarr=np.zeros(3)
print(zerosarr)

ones=np.ones((5,3))
print(ones)

value_arr=np.full((2,4),7)
print(value_arr)

#creating sequences of numbers in numpy
arr=np.arange(1,10,2)
print(arr)

#creating identity matrix
I=np.eye(4)
print(I)