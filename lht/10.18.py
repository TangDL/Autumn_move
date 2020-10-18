import sys
n = int(input())
res = []
for i in range(n):
    s = list(input().split(' '))
    res.append(str(len(s)))
sys.stdout.write(' '.join(res))