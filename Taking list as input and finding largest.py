L = [int(x) for x in input("Enter the numbers ").split()]
i = 1

maximum = L[0]

while i < len(L):
    if maximum < L[i]:
        maximum = L[i]
    
    i = i+ 1

print(maximum)
    
                  
