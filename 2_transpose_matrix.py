X = [[4, 6, 7, 8],
    [3, 7, 2, 7],
    [7, 3, 7, 5]]
result = [[0,0,0,0],
         [0,0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       for K in range(len(X[0])):
           for L in range(len(X[0])):
               result[j][i][K][L] = X[i][j][K][L]

for r in result:
   print(r)
