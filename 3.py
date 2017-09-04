#!/usr/bin/python
import random
r=random.randint(10,66)
print(r)
if r<35:
	print(r)
	print(": is less than 35 \n")
	exit
elif r==30:
	print(" 30 is multiple of 10 and 3, both ")
elif r>=35:
	print(r, " is greater than 35")
else:
	print("your number is : ", r)
