L = [int(x) for x in input("Enter the number ").split()]

zeroCount = 0

Neg = [ ]
Pos = [ ]

for x in L:
    if x == 0:
        zeroCount+= 1
    elif x < 0:
        Neg.append(x)
    else:
        Pos.append(x)

print("Negative Numbers are",Neg)
print("Positive Numbers are",Pos)
print(f"Zero has come {zeroCount} times/times ")

        
    
