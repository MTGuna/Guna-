id=[1,2,3,4,5]
print(id)
x=int(input("enter number:"))
#print(x)
for i in range(len(id)):
    if x==id[i]:
        break
if i<len(id)-1: 
    print(x,"found at position:",i+1)
else:
    print(x,"not found in list")
  
