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
oneball = random.choice(list1)
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
print("Next Pakistan going to Bat")
player1input=input("Player1 hits the ball")
list1=[1,4,6,"out"]
oneball1 = random.choice(list1)
print("random element from the list:",oneball1)
list2=[1,4,6,"out"]
secondball2=random.choice(list2)
print("random element from the list:",secondball2)
list3=[1,4,6,"out"]
thirdball3=random.choice(list3)
print("random element from the list:",thirdball3)
list4=[1,4,6,"out"]
fourthball4=random.choice(list4)
print("random element from the list:",fourthball4)
list5=[1,4,6,"out"]
fifthball5=random.choice(list5)
print("random element from the list:",fifthball5)
list6=[1,4,6,"out"]
sixthball6=random.choice(list6)
print("random element from the list:",sixthball6)
totalscore1=oneball1+secondball2+thirdball3+fourthball4+fifthball5+sixthball6
print("Totalscore:",total1score1)
if totalscore>=totalscore1:
    print("India wins the match")
else:
    print("Pakistan wins the match")




























