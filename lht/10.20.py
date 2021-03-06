import collections


class Solution:
    def __init__(self):
        self.res = []

    def maxFreq(self, s: str, minSize: int) -> int:
        n = len(s)
        occ = collections.defaultdict(int)
        ans = 0
        for i in range(n - minSize + 1):
            cur = s[i: i + minSize]
            occ[cur] += 1
            if occ[cur] > ans:
                self.res = []
                self.res.append(cur)
                ans = occ[cur]
            elif occ[cur] == ans:
                self.res.append(cur)
        return ans


test = Solution()
k = int(input())
s = input()
test.maxFreq(s, k)
res = sorted(test.res)
res = sorted(res, key=lambda i: len(i), reverse=True)
if not res:
    print(-1)
else:
    print(res[0])
