"""2. Listing contents of a directory and making a new directory."""

"""print(dir(os))
print(os.getcwd())
)
"""

#creating a new directory - os.mkdir("newRandomDirectory")


import os

directory2 = "/Users/nunu5/PycharmProjects/plaakshaProject/newRandomDirectory"

content = os.listdir(directory2)

for i in content:
    print(i)



# create directoriesss os.mkdirs("This/ that")
#os.rename("prev name", "new name")
#print(os.environ.get('Path'))


