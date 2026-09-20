#Scalar Multipilication

Matrix = [[1,2,3],
          [7,8,9]]

Number = float(input("Enter the Number you have to multiply "))

Result = [[0,0,0],
          [0,0,0]]

for i in range(len(Matrix)):
            for j in range(len(Matrix[0])):
               Result[i][j] = (Number * Matrix[i][j])

print(Result)
                   
