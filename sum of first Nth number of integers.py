#sum of first Nth number of integers

N = int(input("Enter the Nth Number: "))
Sum = 0
Num = 1
while Num <= N:
    Sum = Sum + Num
    Num = Num + 1
print(Sum)
    
