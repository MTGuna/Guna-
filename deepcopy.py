import copy
list=[[1,2,3],[4,5,6],[7,8,9]]
list1=copy.deepcopy(list)
print(list1)
list1[1][1]=10
print("list:",list)
print("New list:",list1)
