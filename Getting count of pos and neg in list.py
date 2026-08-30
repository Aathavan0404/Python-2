L = [int(x) for x in input("Enter the numbers ").split()]

negCount = 0
posCount = 0
zeroCount = 0

for x in L:
    if x < 0:
        negCount += 1
    elif x > 0:
        posCount += 1
    else:
        zeroCount += 1

print("Negative numbers count =",negCount)
print("Positive numbers count =",posCount)
print("Zero count =",zeroCount)


        
