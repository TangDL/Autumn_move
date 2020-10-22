from collections import defaultdict
import queue
import sys
graph, opp_graph, out = defaultdict(list), defaultdict(list), defaultdict(int)
n, m = map(int, input().split())

q = queue.PriorityQueue()
for _ in range(m):
    x, y = map(int, (input().split()))
    graph[x].append(y)
    opp_graph[y].append(x)
for d in range(1, n + 1):
    out[d] = len(graph[d])
    if out[d] == 0:
        q.put(-d)
ans, count = [0 for i in range(n)], n
while not q.empty():
    node = -q.get()
    ans[node - 1] = count
    count -= 1
    for d in opp_graph[node]:
        out[d] -= 1
        if out[d] == 0:
            q.put(-d)
res = list(map(str, ans))
sys.stdout.write(res[0])
sys.stdout.write(' ')
sys.stdout.write(res[-1])