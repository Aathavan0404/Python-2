num = int(input('Enter the number'))

Reverse = 0

while num>0:
    digit = num%10
    Reverse = Reverse*10 + digit
    num = num//10
print(Reverse)

