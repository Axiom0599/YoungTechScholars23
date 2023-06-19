# Write ‘x’ and ‘y’ separated by a comma to a file."""

from file2 import x
from file2 import y

with open("file2.py", 'r') as file:
    file.read()

with open("file2.py",'a') as file:
    file.write("Comma separated values: " + str(x) + "," +  str(y))
