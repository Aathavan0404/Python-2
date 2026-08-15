#Multiple conditions

Marks = int(input("Enter the marks: "))
if (Marks > 100) or ( Marks < 0):
    print("Invalid Marks")
elif Marks >= 75:
    print("A")
elif Marks>= 65:
    print("C")
elif Marks>=50:
    print("C")
elif Marks >=35:
    print("S")
else:
    print("W")
