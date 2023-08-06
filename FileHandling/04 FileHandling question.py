''' Repeat program for a list of such words to be censored. You need to write a 
program which replaces this word with $%^@%^# by updating the same file '''

words = ["Donkey", "kaddu", "mota"]

with open("samples.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^@%^#")

with open("sample.txt", "w") as f:
    f.write(content)