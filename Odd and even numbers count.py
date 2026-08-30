L = [int(x) for x in input("Enter the numbers ").split()]

oddCount = 0
evenCount = 0
zeroCount = 0

#i = 0
#while i < len(L):

for x in L:
    if x == 0:
        zeroCount += 1
    elif x % 2 == 1:
        oddCount += 1
    else:
        evenCount += 1

# i = i + 1

print("Odd numbers count =",oddCount)
print("Even numbers count =",evenCount)
print("Zero count =",zeroCount)s


