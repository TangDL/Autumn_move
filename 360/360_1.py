
def main():
    [a, b, k, v] = list(map(int, input().split()))
    res = 0
    if b >= k-1:
        geban_box = b // (k-1)
        shenyu_geban = b % (k-1)
        for i in range(1, geban_box+1):
            n_geban_box = i * k * v
            if n_geban_box >= a: return i
        res += geban_box
        shenyu_wuti = a - n_geban_box
        shenyu_wuti -= (shenyu_geban +1) * v
        res += 1
        if shenyu_wuti <= 0: return res
        else:
            res += (shenyu_wuti // v) + (1 if shenyu_wuti % v != 0 else 0)
            return res
    else:
        res += 1
        shenyu_wuti = a - (b+1)*v
        if shenyu_wuti<=0: return res
        res += (shenyu_wuti // v) + (1 if shenyu_wuti % v != 0 else 0)


def main1():
    [a, b, k, v] = list(map(int, input().split()))
    res = 0

    for i in range(1, b+1):
        if i % (k-1) == 0:
            res +=1
            a -= (2*v)
        else:
            a -= v
        if a <= 0: return res

    res += (a//v) + (1 if a%v !=0 else 0)
    return res

while 1:
    res = main()
    print(res)