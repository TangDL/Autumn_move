
def sheep():
    [f, s, m, n] = list(map(int, input().split()))

    dp = [0]*m
    dp[0] = 1
    for i in range(2, n+1):
        for j in range(m-2, 0, -1):
            dp[j] = dp[j-1]
        dp[m-1] += dp[m-2]
        dp[0] = dp[f-1] + dp[s-1]
    return sum(dp[:-1])

res = sheep()
print(res)

# 2 4 5 15