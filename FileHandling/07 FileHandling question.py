# Write a program to find out whether a file id identical & matches the content of another file

file1 = "this.txt"
file2 = "this(copy).txt"

with open(file1) as f:
    f1 = f.read()
with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("The file content are identical & matches")
else:
    print("The file content are not identical & matches")