import sys
n = int(input())
arr = list(map(int, input().split()))


def fun(arr, n):
    arr2 = sorted(arr)
    p, q = n-1, n-1
    while p >= 0 and q >= 0:
        if arr[p] == arr2[q]:
            p -= 1
            q -= 1
        else:
            while p >= 0 and arr[p] != arr2[q]:
                p -= 1
    return q+1


sys.stdout.write(str(fun(arr, n)))