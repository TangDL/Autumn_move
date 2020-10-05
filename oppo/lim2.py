N = int(input())
dp = [0]*(N)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, N):
    a = i
    dp[i] += dp[a-1]
    while a-2 >= 0:
        dp[i] += dp[a-2]
        a -= 2
print(dp[N-1])
# import sys
# def frog(N):
#     if N<=1: return N
#     dp = [0]*(N+1)
#     dp[0], dp[1], dp[2] = 0, 1, 1
#     for i in range(3, N+1):
#         k = 0
#         while pow(2, k)+1 <= i:
#             temp = dp[i - pow(2, k)]
#             dp[i] += temp
#             k += 1
#     return dp[-1]
#
# n = int(input())
# res = frog(n)
# sys.stdout.write('%d'%res)