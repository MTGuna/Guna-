def changeover(mylist,mylist1):
    #mylist=[1,2,3,4,5]
    #mylist2=[4,5,6,7,8]
    print("ID:",id(mylist))
    print("ID1:",id(mylist1))
    print("mylist:",mylist)
    print("mylist1:",mylist1)
    mylist[1]=10
    mylist1[2]=9
    print("list:",mylist)
    print("LIST:",mylist1)
    print(type(mylist1))
mylist=[1,2,3,4,6]
mylist1=[4,5,6,7,8]
print(mylist)
print(len(mylist))
changeover(mylist,mylist1)
print("outside:",mylist)
