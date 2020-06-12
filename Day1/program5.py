score1=int(input("Enter the runs of player1 on 60 balls: "))
score2=int(input("Enter the runs of player2 on 60 balls: "))
score3=int(input("Enter the runs of player3 on 60 balls: "))
strike_rate1=(score1/60)*100
strike_rate2=(score2/60)*100
strike_rate3=(score3/60)*100
print("Strike rate of player 1 : ",strike_rate1)
print("Strike rate of player 2 : ",strike_rate2)

print("Strike rate of player 3 : ",strike_rate3)
print("Runs scored by player 1 if 60 more balls: ",score1*2)
print("Runs scored by player 2 if 60 more balls: ",score2*2)
print("Runs scored by player 3 if 60 more balls: ",score3*2)
print("Maximum sixes by player 1: ",score1//2)
print("Maximum sixes by player 2: ",score2//2)
print("Maximum sixes by player 3: ",score3//2)
