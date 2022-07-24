

# ipdb.set_trace()
matrix = [[1, 2, 3],
          [4, 5, 6]]
matrix1 = [[7, 8],
           [9, 10],
           [11, 12]]
row = 2
col = 3
row1 = 3
col1 = 2

result = [[0,0],
          [0,0]]

a = []
# adding two matrices

for i in range(len(matrix)):
    ans = 0
    for k in range(len(matrix1[0])):

        ans1 =0
        for j in range(len(matrix1)):


            result[i][k] += (matrix[i][j] * matrix1[j][i])
            #print("ans is ",ans)
                #ans1 = ans1 + (matrix[i][j] * matrix1[i][j])

        #a.append(ans1)



print("Here is the final matrix..........")
print(result)



