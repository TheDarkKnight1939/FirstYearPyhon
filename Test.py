#!usr/bin/python3
g=int(input("Enter your Marks:  "))
if g>100:
	print("Marks should be lesser then 101")
elif g>=90:
	print("A Grade")
elif g>=80:
	print("B Grade")
elif g>=70:
	print("C Grade")
elif g>=60:
	print("D Grade")
else:
	print("E Grade")

