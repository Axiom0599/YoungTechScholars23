"""
1. Open a .txt file and learn to write data and append to to it.
2. Listing contents of a directory and making a new directory.
3. Writing 12345 using loops in same line and new lines.
4. Read .txt file and print all the its contents.
5. Read line-by-line
6. Read from a file and write the multiplied number to another file.
7. Write ‘x’ and ‘y’ separated by a comma to a file."""

#************************************************** TASK 1  **************************************************************************

#opening a file
file1 = open("random_file.txt", 'w')

#writing in the file
file1.write("hello ashira")
file1.close()

#appending the data

file2 = open("random_file.txt", 'a')
file2.write("Welcome")
file2.close()

#************************************************** TASK 2  **************************************************************************


