def oppo1():
    t = int(input())
    for i in range(t):
        [H, W, K] = list(map(int, input().strip().split()))
        visited = [[0]*W for _ in range(H)]
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(x, y):
            if x < 0 or y < 0 or x >= W or y >= H:
                return
