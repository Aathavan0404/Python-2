a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

import math

delta = b**2 - 4*a*c
if delta == 0:
    x = -b/(2*a)
    print(x)
elif delta < 0:
    print("Imaginary solutions")
else:
    x = (-b + math.sqrt(delta))/2*a
    print(x)
    x = (-b - math.sqrt(delta))/2*a
    print(x)
