#! python3

x = input("Enter an integer")
y = input("Enter an interger")
z = input("Enter an interger")
x = int(x)
y = int(y)
z = int(z)
c = max(x,y,z)
a = min(x,y,z)
mylist = [x,y,z]
b = sorted(mylist)[len(mylist) // 2]
g = str(a) + "," + str(b) + "," + str(c)
if a ** 2 + b ** 2 == c ** 2:
 print("that is a right triangle")
else:
print("NONE")





"""
Open the file called problem4.py
Have the user enter in 3 numerical values, representing the side lengths of a triangle.
Determine if the values are close enough to make a right triangle.
(It is close enough if the expected length of the hypotenuse and the actual 
length differ by no more than 2%)
(2 marks)

# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
