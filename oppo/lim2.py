N = int(input())
dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, N+1):
    a = i
    dp[i] += dp[a-1]
    while a-2 >= 0:
        dp[i] += dp[a-2]
        a -= 2
print(dp[N-1])
