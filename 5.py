#usr/bin/python3
mypos=0
import random
while mypos<=100:
	r=random.randint(1,6)
	print("Number got when the dice is rolled =" , r)
	while r==8 or r==2:
		r=r+r
		exit()
		



	


	
 


