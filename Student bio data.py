N = int(input("How many students: "))
i = 0

Names = [ ]
Indexs = [ ]
Marks1 = [ ]
Marks2 = [ ]
Marks3 = [ ]
Results = [ ]

for i in range(0,N):
    Name = input("Enter the student's name ")
    Names.append(Name)
    
    Index = input("Enter the student's index Number ")
    Indexs.append(Index)
    
    Marks = [int(x) for x in input("Enter the marks with space: ").split()]
    
    Marks1.append(Marks[0])
    Marks2.append(Marks[1])
    Marks3.append(Marks[2])
    Average = ( Marks [0] + Marks [1] + Marks [2] )/3
    
    if Average > 50:
        Result = "Pass"
        Results.append(Result)
        print("Result of",Names[i],"is",Result)
    else:
        Result = "Fail"
        Results.append(Result)
        print('Result of',Names[i],"is",Result)
        
print(Names,";",Results)

        
    
    
    
    
    
    
