#required argument
def sum(str):
    print(id(str))
    print(str)
str=("hello")
sum(str)

#keyword arg
def key(name,age):
    print("Name:",name)
    print("Age:",age)
key("guna",21)
key(age=21,name="guna")

#default
def default(name="guna",age=20):
    print("Name:",name)
    print("Age:",age)
default()

#variable length agrument
def var(name,*age):
    print("Name:",name)
    print("Age:",age)
    for var in age:
        print(var)
    return
var("guna",10,20,30,40)

#anonymous function
sum= lambda arg1,arg2:arg1+arg2
print(sum(10,20))

#scope of variables
total=2
def scope(a,b):
    total=a+b
    print(total)
    return total
scope(10,20)
print("sum:",total)

#return
def scope(a,b):
    total=a+b
    print(total)
    return total
total=scope(10,20)
print("sum:",total)

    
