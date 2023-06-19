"""6. Read from a file and write the multiplied number to another file."""

from file1 import product1
from file1 import num1
from file1 import num2

with open("file1.py", 'r') as file:
    data = file.read()


with open("file1.py", 'a') as file:
    file.write("The product of the two numbers is: "+ str(num1*num2))




