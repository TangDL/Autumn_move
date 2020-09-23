
def movingCount(m: int, n: int, k: int) -> int:
    def movesum(x, y):
        tmp = list(str(x)+str(y))
        res = 0
        for i in tmp:
            res += int(i)
        return res
    q = [(0, 0)]
    s = []
    while q:
        x, y = q.pop(0)
        if (x, y) not in s and 0<=x<m and 0<=y<n and movesum(x, y)<=k:
            s.append((x,y))
            for nx, ny in [(x+1, y), (x, y+1)]:
                q.append((nx, ny))
    return len(s)


t = int(input())
for i in range(t):
    H, W, K = list(map(int, input().split()))
    print(movingCount(H, W, K))