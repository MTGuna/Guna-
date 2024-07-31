import random
list=["player1","player2","player3"]
print(list)
player1_score=1000
player2_score=1000
player3_score=1000
first=random.choice(list)
print("Random element from the list:",first)
if first=="player1":
    player1_score=1000
if first=="player2":
    player2_score=1000
if first=="player3":
    player3_score=1000
second=random.choice(list)
print("Random element from the list:",second)
if second=="player1":
    player1_score=1000
if second=="player2":
    player2_score=1000
if second=="player3":
    player3_score=1000
third=random.choice(list)
print("Random element from the list:",third)
if third=="player1":
    player1_score=1000
if third=="player3":
    player2_score=1000
if third=="player3":
    player3_score=1000
if(player1_score>player2_score) & (player1_score>player3_score):
    print("player1 wins the competition")
if(player2_score>player1_score) & (player2_score>player3_score):
    print("player2 wins the competition")
if(player3_score>player1_score) & (player3_score>player2_score):
    print("player3 wins the competition")
