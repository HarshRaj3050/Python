print("Enter the number : ")
n = int(input())
sum = 0
avg = 0.0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print("sum is : ", sum)
avg = sum / n
print(f"Average is : {avg}")