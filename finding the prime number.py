#finding the prime number

N = int(input("Enter the Number: "))

if N < 1:
    print(N,"is not a prime number")
else:
    prime = True
    for i in range(2,N):
        d = N%i
        if d == 0:
            prime = False
            break
    if prime:
        print("Prime number")
    else:
        print("Not a prime Number")

        
    
            
