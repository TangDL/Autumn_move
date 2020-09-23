
def dikaer_product(*args):
    pools = map(tuple, args)
    temp = [[]]
    for pool in pools:
        temp = [x + [y] for x in temp for y in pool]
    return temp

nums = [['aa', 'bb', 'cc'], ['AA', 'BB'], ['11', '22']]

print(dikaer_product(*nums))