''' A file contains a word "Donkey" multiple times. You need to write a 
program which replaces this word with $%^@%^# by updating the same file '''

with open("samples2.txt") as f:
    content = f.read()
content = content.replace("Donkey", "$%^@%^#")
with open("samples2.txt", "w") as f:
    f.write(content)
