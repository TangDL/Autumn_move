m = int(input())
n = int(input())
matrix = []
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(int(input()))
    matrix.append(tmp)
def diagonal_left(matrix):
    if not matrix:
        return []
    row = len(matrix)
    col = len(matrix[0])
    k=0
    result = []
    for i in range(row):
        for j in range(k,col): # j顺序遍历
            i1, j1 = i, j # i1,j1用于方便同一对角线元素的添加，否则改变i,j影响开头元素的选择
            while i1 <= row - 1 and j1 >=0:
                result.append(str(matrix[i1][j1]))
                j1 -= 1
                i1 += 1
            if i==0 and j==col-1:
                k=col-1
    return result

res = diagonal_left(matrix)
print(','.join(res))