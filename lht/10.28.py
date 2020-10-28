import sys
class Solution:
    def spiralOrder(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        x = [0, 1, 0, -1]
        y = [1, 0, -1, 0]
        xp, yp = 0, 0
        direction = 0
        res = [str(matrix[xp][yp])]
        matrix[xp][yp] = '#'
        while len(res)<row*col:
            tmpx = xp + x[direction%4]
            tmpy = yp + y[direction%4]
            if 0<=tmpx<row and 0<=tmpy<col and matrix[tmpx][tmpy]!='#':
                xp = tmpx
                yp = tmpy
                res.append(str(matrix[xp][yp]))
                matrix[xp][yp] = '#'
            else:
                direction += 1
        return res


m = list(input().split('#'))
matrix = []
for i in range(len(m)):
    tmp = list(map(int, m[i].split(',')))
    matrix.append(tmp)
test = Solution()
res = test.spiralOrder(matrix)
sys.stdout.write(','.join(res))