import random
print("Match is going to start")
print("India VS Pakistan")
print("Lets begin with the Toss")
cricketinput=input("Spin the coin:")
list=["Head","Tail"]
toss=random.choice(list)
print("random element from the list:",toss)
if cricketinput in list:
    print("choice goes to the toss thrown team")
else:
    print("choice goes to the opponent team")
print("Batting")
print("India is going to bat")
player1input=input("Player1 hits the ball")
list1=[1,4,6,"out"]
oneball= random.choice(list1)
print("random element from the list:",oneball)
list2=[1,4,6,"out"]
secondball=random.choice(list2)
print("random element from the list:",secondball)
list3=[1,4,6,"out"]
thirdball=random.choice(list3)
print("random element from the list:",thirdball)
list4=[1,4,6,"out"]
fourthball=random.choice(list4)
print("random element from the list:",fourthball)
list5=[1,4,6,"out"]
fifthball=random.choice(list5)
print("random element from the list:",fifthball)
list6=[1,4,6,"out"]
sixthball=random.choice(list6)
print("random element from the list:",sixthball)
totalscore=oneball+secondball+thirdball+fourthball+fifthball+sixthball
print("Totalscore:",totalscore)
