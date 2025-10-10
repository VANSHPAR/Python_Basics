import numpy as np
arr=np.array([[1,2,np.nan,4,5],[7,8,9,np.nan,10]])
print(np.isnan(arr))

#To replace nan with num
new_arr=np.nan_to_num(arr,nan=100)
print(new_arr)


#Handle infinite numbers
arr=np.array([1,2,np.inf,4,5*np.inf,6])
print(np.isinf(arr))

new_arr=np.nan_to_num(arr,posinf=1000)
print(new_arr)