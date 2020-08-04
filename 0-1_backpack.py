C = 15
W = [3,7,11,9]
V = [4,1,6,3]
n = len(W)


"""O(C*n)"""
dp = [[0 for i in range(C+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1, C+1):
        if j >= W[i-1]:
            dp[i][j] = max(dp[i-1][j-W[i-1]] + V[i-1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][C])

"""O(C),减少空间复杂度"""
dp = [0 for i in range(C+1)]

for i in range(1, n):
    for j in range(C, 0, -1):
        if j >= W[i-1]:
            dp[j] = max(dp[j], dp[j-W[i-1]] + V[i-1])
print(dp[C])


