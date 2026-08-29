L = [int(x) for x in input("Enter the numbers seperated by space ").split()]

print(L)

odd=[ ]
even=[ ]

for x in L:
    if x%2==1:
        odd.append(x)
    else;
        even.append(x)

print("Odd numbers are",odd)
print("Even numbers are",even)
      
    
