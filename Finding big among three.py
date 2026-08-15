#Finding the Largest number among three
A = float(input("Enter the Number "))
B = float(input("Enter the Number "))
C = float(input("Enter the Number "))

if A>B:
    if A>C:
        print(A)
    else:
        print(C)
else:
    if B>C:
        print(B)
    else:
        print(C)
        
