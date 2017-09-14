#!/usr/bin/python3
import random #*Uses Random Module
n=(int(input("press 7 to play")))
i=0
j=0
while(n==7):#The program gives the program a prompt everytime to run the program.
	t=["Rock","Paper","Scissors"]
	Computer=t[random.randint(0,2)]#The choice of the computer is taken using the random function.
	print("Enter your Choice:-")
	Player=input("Rock, Paper, Scissors") #The user is asked to input his choice (A choice between Rock Paper and Scissors).
	if(Computer==Player): #A series of if else-if statements is used to compare the choices of the computer and the player.
		print("Tie!")
		print("Both the Players played ", Computer) #Based on the comparision, the program displays the result based on the comparison.
	elif(Computer=="Rock"):
		if(Player=="Paper"):
			print("The computer played: ",Computer)
			print("The Player played: ",Player)
			print("The Paper Wraps the Stone!")
			print("Player Wins!")#Based on the comparision, the program displays the result based on the comparison.
			i=i+1
		else:
			print("Computer Wins")
			j=j+1
	elif(Computer=="Paper"):
		if(Player=="Scissors"):
			print("The computer played: ",Computer)
			print("The Player played: ",Player)
			print("The Scissors Cuts Paper!")#Based on the comparision, the program displays the result based on the comparison.
			print("Player Wins!")
			i=i+1
		else:
			print("Computer Wins")#Based on the comparision, the program displays the result based on the comparison.

			j=j+1
	elif(Computer=="Scissors"):
		if(Player=="Rock"):
			print("The computer played: ",Computer)
			print("The Player played: ",Player)
			print("Rock Breaks the Scissors")#Based on the comparision, the program displays the result based on the comparison.
			print("Player Wins!")#Based on the comparision, the program displays the result based on the comparison.
			i=i+1
		else:
			print("Computer Wins")#Based on the comparision, the program displays the result based on the comparison.
			j=j+1
	else:
		print("Enter Choice again")
	if(i>j):#Another module is included to count the scores of the computer and player based on the if else-if statements used above.
		print("Player leads by ",i-j)
	elif(i==j):
		print("The Scores are tied at ",i)
	else:
		print("Computer leads by ",j-i)





			



	
