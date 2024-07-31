import random
#choice() function
print("random number from range(50):",random.choice(range(50)))
list=[1,2,3,4,49]
print("Random element from the list:",random.choice(list))
str="hello world"
print("random character from the string:",random.choice(str))

#random() function
#fisrt random number
print("random():",random.random())

#second random number
print("random():",random.random())

random.seed(10)
print("random number with int seed",random.random())

#shuffle() function
list=[12,1,2,4,5]
random.shuffle(list)
print("Reshuffled list:",list)

#uniform() function
print("Random float uniform(6,10):",random.uniform(6,10))
print("Random float uniform(7,10):",random.uniform(7,10))


import random as rd

print(rd.randrange(6,10))
print(rd.randrange(5,10,2))
