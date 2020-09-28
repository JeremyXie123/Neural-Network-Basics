import numpy as np

vec = [1,2,3]
vec2 = [3,2,1]

tbl1 = [[2,4,6],[2,4,6],[2,4,6]]

print(np.dot(vec,tbl1))
# dot between each sub vec of tbl and each component of vec

print(np.dot(tbl1,vec))
# dot between vec and each sub vec of tbl1

for k,v in zip(vec,vec2):
    print(k,v)

print(vec[1:], vec[:-1])
