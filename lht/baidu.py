import sys
class Solution(object):

    def getmax(self, lists):
        if lists == [] or not lists:
            return 0

        row = len(lists)
        col = len(lists[0])
        res = 0
        dp = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    if lists[i][j] == 1:
                        dp[i][j] = 1
                        res = 1

        for i in range(row):
            for j in range(col):
                if lists[i][j] == 'M':
                    mins = min(dp[i - 1][j], dp[i][j - 1])
                    dp[i][j] = min(dp[i - 1][j - 1], mins) + 1

                res = max(res, dp[i][j])

        return res


if __name__ == "__main__":
    sol = Solution()
    m, n = list(map(int, input().split()))
    lists = []
    for i in range(m):
        lists.append(list(input()))
    # lists = [['M', 'M', 'M', 'M'], ['M', 'M', 'F', 'F'], ['F', 'M', 'M', 'M'], ['M', 'M', 'M', 'M'], ['M','M','M','M']]
    maxvalue = sol.getmax(lists)
    sys.stdout.write(str(maxvalue**2))