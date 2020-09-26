import sys
def find():
    [n, m, k] = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    visited = [0] * n

    def dfs(start, temp):
        if len(temp) == m:
            if sum(temp)%k == 0: return True
            else: return False
        for i in range(start, n):
            if not visited[i]:
                visited[i] = 1
                temp.append(nums[i])
                if dfs(i+1, temp):
                    return True
                visited[i] = 0
                temp.pop()
        return False
    return dfs(0, [])

d = int(input())
for i in range(d):
    if find(): sys.stdout.write('%s'%'Yes')
    else: sys.stdout.write('%s'%'No')


