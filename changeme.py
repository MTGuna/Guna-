def changeme(mylist):
    mylist=[1,2,3,4]
    print("mylist:",id(mylist))
    print("mylist:",mylist)
mylist=[10,20,30]
print(id(mylist))
changeme(mylist)
print(mylist)   
def change(mylist):
    print(id(mylist))
    print("inside before change:",mylist)
    mylist[2]=50
    print("after chaneg:",mylist)
mylist=[10,20,30]
print(id(mylist))
change(mylist)
print("outside:",mylist)
