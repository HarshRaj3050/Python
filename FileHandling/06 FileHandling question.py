# Write a program to make a copy of a lext file "this.txt"

with open("this.txt") as f:
    content = f.read()

with open("this(copy).txt", "w") as f:
    f.write(content)