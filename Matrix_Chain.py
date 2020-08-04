DIMS = [30, 35, 15, 5, 10, 20, 25]

n = len(DIMS) - 1
M = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    M[i][i] = 0
for l in range(2, n+1):
    for i in range(1, n-(l-1)+1):
        j = i + l - 1
        M[i-1][j-1] = float('inf')
        for k in range(i, j):
            q = M[i-1][k-1] + M[k][j-1] + DIMS[i-1]*DIMS[k]*DIMS[j]
            print(q)
            if q < M[i-1][j-1]:
                M[i-1][j-1] = q

print(M)
