#! python3

x = input("Enter one side:")
y = input("Enter a second side:")
z = input("Enter third side:")
x = float(x)
y = float(y)
z = float(z)
c = max(x,y,z)
a = min(x,y,z)
mylist = [x,y,z]
b = sorted(mylist)[len(mylist) // 2]
g = float(a) + "," + float(b) + "," + float(c)
if a ** 2 + b ** 2 == c ** 2:
 print("that is a right triangle")
else:
 if a ** 2 + b ** 2 > c ** 2:
  print ("that is an acute triangle")
 else:
  if a ** 2 + b ** 2 < c ** 2:
   print ("that is an obtuse triangle")

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
