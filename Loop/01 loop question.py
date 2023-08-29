''' Write a python program for computing the sum of n natural numbers and 
    numbers and finding out the average of it. '''

num = int(input("Enter the Number : "))
sum = 0
i = 1
while(i <= num):
    sum = sum + i
    i = i+1
avg = sum % num
print(f"The sum of {num} Natural number is : {sum}")
print(f"The average of {num} Natural number is : {avg}")

