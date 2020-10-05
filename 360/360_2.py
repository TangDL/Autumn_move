from collections import defaultdict
def main():
    [n, m, s, t] = list(map(int, input().split()))
    maps = defaultdict(list)
    for i in range(m):
        [u, v, w] = list(map(int, input().split()))
        maps[u].append([v, w])

    res = float('inf')
    visited = [False]*(n+1)
    ans = 0
    def dfs(pos, cur, temp):
        nonlocal res, ans
        if pos == t:
            if cur < res:
                res = cur
                ans = max(temp)
            return
        else:
            visited[pos] = True
            for v, w in maps[pos]:
                if not visited[v]:
                    temp.append(w)
                    dfs(v, cur+w, temp)
                    temp.pop()
            visited[pos] = False
    dfs(s, 0, [])
    print(ans)
    return res

main()



