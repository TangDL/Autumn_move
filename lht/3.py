_, __, ___, n = list(map(int, input().split()))
def num(n):
    m = 1
    for i in range(1, n+1):
        if i == 2:
            m += num(n-2)
        elif i == 4:
            m += num(n-4)
        elif i == 5:
            m -= 1
    return m

print(num(n))