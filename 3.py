#!/usr/bin/python
import random #Imports the class random
r=random.randint(10,66) #Uses the randint function to choose a number from 10 to 66 
print(r) #Prints the random number choosen
if r<35: #If loop which checks if the number is lesser than 35 
	print(r)
	print(": is less than 35 \n")
	exit
elif r==30:#If loop which checks if the number is equal to 30
	print(" 30 is multiple of 10 and 3, both ")
elif r>=35:#If loop which checks if the number is lesser than 35
	print(r, " is greater than 35")
else:
	print("your number is : ", r)
