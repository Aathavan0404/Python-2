res = 1
i = 0

for i in range(0,10):
    num = int(input("Enter the number "))
    if num > 0:
        res = res*num

print('Multipilication of positive numbers is',res)
