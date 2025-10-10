import numpy as np
prices=np.array([100,200,300,4444,500])

discount=10

final_prices=prices-(prices*(discount/100))
print(final_prices)


#Broadcasting for 1d to 2d array
matrix=np.array([[1,1,3],[2,4,5]])
vector=np.array([10,20,30])
res=matrix+vector
print(res)


#Incompatible shapes
# matrix=np.array([[1,1,3],[2,4,5]])
# arr2=np.array([1,2])
# res=matrix+arr2
# print(res)

