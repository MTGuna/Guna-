list1=["physics","chemistry",1997,2000]
list2=[1,2,3,4,5,6,7]
print("list1[2]:",list1[2])
print("list2[4]:",list2[4])

#update
print("values available at index1:",list1[1])
print(list1[1])
list1[1]="maths"
print("new values in index1:",list1[1])
print(list1[1])
#delete
print(list1)
del list1[2]
print("after deleting the value in list1:",list1[2])
print(list1)
print(list2)
del list2[5]
print("after deleting the value in list2:",list2[5])
print(list2)
