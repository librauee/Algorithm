A = 'ABCBDAB'
B = 'BDCABA'
m = len(A) + 1
n = len(B) + 1

C = [[0 for i in range(n)] for j in range(m)]
D = [[0 for i in range(n)] for j in range(m)]

for i in range(1, m):
    for j in range(1, n):
        if A[i-1] == B[j-1]:
            C[i][j] = C[i-1][j-1] + 1
            D[i][j] = 'NW'
        elif C[i-1][j] > C[i][j-1]:
            C[i][j] = C[i-1][j]
            D[i][j] = 'N'
        else:
            C[i][j] = C[i][j-1]
            D[i][j] = 'W'

print(C)
print(D)

def print_LCS(D, A ,i ,j):
    if i == 0 or j == 0:
        return
    if D[i][j] == 'NW':
        print_LCS(D, A, i-1, j-1)
        print(A[i-1])
    elif D[i][j] == 'N':
        print_LCS(D, A, i-1, j)
    else:
        print_LCS(D, A, i, j-1)

print_LCS(D, A, m-1, n-1)
