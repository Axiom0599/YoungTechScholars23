
a = open('task 6','r')
b = open('task 6', 'a')

lines = a.readlines()

for line in lines:
    number = int(line.strip("\n"))
    b.write("The product of the two numbers is "+str(number*number))