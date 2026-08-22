N = int(input("Enter the Number "))
T = 1
X = int(N/T)

while T<=N:
    if N%T == 0:
        if T<X:
            X = int(N/T)
            print(N,"=",T,"*",X)
    T = T + 1
        
        
    
