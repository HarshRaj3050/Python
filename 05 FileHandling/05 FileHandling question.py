''' Write a program to mine a log file and find out whether it contains 'python'
and find out the line number where python is present '''

content = True
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline()
        if "python" in content.lower():
            print(f"Python is present in log file, line number {i}")
        i+=1
        