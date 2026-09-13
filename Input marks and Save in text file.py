f = open("Subjects.txt","w")

Index = int(input("Enter the index no: or Enter -1 to stop "))

while Index != -1:
    Marks1 = float(input("Enter the marks 1 : "))
    Marks2 = float(input("Enter the marks 2 : "))
    Marks3 = float(input("Enter the marks 3 : "))
    Data = f"Index No - {Index}, Marks are {Marks1},{Marks2},{Marks3}\n "
    f.write(Data)
    Index = int(input("Enter the index no: or Enter -1 to stop "))

f.close()
    
    
    
    
