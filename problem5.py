#! python3
import math

a = input("Enter a:")
b = input("Enter b:")
c = input("Enter c:")

x = int(b)^2 - 4 * int(a) * int(c)

number = int(input(x))

root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print("the equation can be factored")
else:
    print("the equation can not be factored")

"""
In math, if a quadratic equation is in the format
ax^2 + bx + c = 0, the discriminant can be calculated as
b^2 - 4 * a * c
If the discriminant is a perfect square, the equation can
be factored.  Furthermore, if the discriminant is negative,
then the equation has no solutions (not used in this assignment).
Have the user enter in values for a, b and c and then 
tell them if the equation can be factored.

Inputs:
- 3 numbers (a, b, c)

Outputs:
- "the equation can be factored"
- "the equation can not be factored"

Example:
Enter a: 1
Enter b: 4
Enter c: 4
the equation can be factored

Enter a: 1
Enter b: 4
Enter c: 8
the equation can not be factored
"""