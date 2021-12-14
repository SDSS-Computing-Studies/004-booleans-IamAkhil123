#! python3 

x = input("Enter a number")
if float(x) == 1000 or float(x) > 1000:
 print("3")
if float(x) == 100 or float(x) < 1000 and float(x) > 100:
 print("2")
if float(x) == 10 or float(x) < 100 and float(x) > 10:
 print("1")
if float(x) == 0 or float(x) < 10:
 print("0")

"""
Open the file called task3.py
Have the user enter a number.
Use an if...elif statement to determine if the number is
a) larger than 1000
b) larger than 100
c) larger than 10
d) larger than 0
Output must match one of the valid output statements listed in the program
(2 points)

Inputs:
a number

Output is a single number that represents a range of numbers:
"3" : The number is equal to 1000 or is larger than 1000
"2" : The number is 100 or a number up to 1000 
"1" : The number is 10 or a number up to 100 
"0" : The number is 0 or a number up to 100 

Example:
Enter a number: 3
0

Enter a number: 212
2

Enter a number: 10000
3


"""