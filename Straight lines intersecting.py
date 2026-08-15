#Straight lines intersecting point

m = int(input('Enter m '))
M = int(input('Enter M '))
c = int(input('Enter c '))
C = int(input('Enter C '))

if M == m:
    print("Parallel Lines")
else:
    x = (C - c)/( m - M )
    y= (M*c - m*C)/( M - m )
    print(x)
    print(y)
    
