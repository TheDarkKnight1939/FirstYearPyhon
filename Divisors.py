#!/usr/bin/python3
g=(int(input("Enter a number ")))
print("The divisors are :-")
i=1
for i in range(1,g):
	if(g%i==0):
		print(i)
	else:
		i=i+1