import numpy as np
arr=np.array([1,2,3,5])
print(arr)
new_arr=np.insert(arr,2,30,axis=0)
#axis=0 insert ele row wise axis=1 insert ele col wise
print(new_arr)

arr1=np.array([[1,2],[3,5]])
print(arr1)
new_arr=np.insert(arr1,1,[5,6],axis=0)
print(new_arr)
new_arr1=np.insert(arr1,1,[5,6],axis=1)
print(new_arr1)

#Append function
print("------append-------")
arr=np.array([1,2,3,5])
new_arr=np.append(arr,6)
print(new_arr)

#Concatenate function
print("-------concatenate------")
arr1=np.array([1,2,3,5])
arr2=np.array([7,9,11,15,17])
arr3=np.concatenate((arr1,arr2),axis=0)
print(arr3)


#delete function
print("-------Delete------")
arr=np.array([1,3,5,8,96,4])
new_arr=np.delete(arr,1)
print(new_arr)

arr2d=np.array([[1,2,3],[4,5,6]])
new_arr=np.delete(arr2d,1,axis=0)
print(new_arr)

#Stacking -> combines multiple arrays vertically and horizontally
print("------Stacking-----")
arr1=np.array([1,2,3,5])
arr2=np.array([7,9,11,15])

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))


#Spliting -> divide array into multiple parts
print("--------Spliting---------")
arr=np.array([10,20,30,40,50,60,70,80,90,100])
print(np.split(arr,5))

arr2d=np.array([[1,2,3],[4,5,6]])
print(np.vsplit(arr2d,2))

arrd=np.array([[1,2],[4,5]])
print(np.hsplit(arrd,2))