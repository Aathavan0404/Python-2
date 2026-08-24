#Finding Fctorial of a number

n = int(input("Enter the Number "))
fact = 1
turn = 1

while turn <= n:
    fact = fact*turn
    turn = turn + 1

print(fact)
    
    
