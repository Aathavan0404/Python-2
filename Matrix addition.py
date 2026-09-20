#Matrix addition

Matrix1 = [[1,2,3],
           [4,5,6]]

Matrix2 = [[7,8,9],
           [10,11,12]]

result = [[0,0,0],
          [0,0,0]]

for i in range(len(Matrix1)): #0,1

    for j in range(len(Matrix1[0])): #0,1,2

        result[i][j] = Matrix1[i][j] + Matrix2[i][j]

print(result)
