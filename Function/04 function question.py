''' 
Write a python function to print first n lines of the following pattern.
   ****
   ***           n = 4
   **
   *    
'''

n = 4
for i in range(n): 
    print("*" * (n-i))