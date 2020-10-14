import itertools
state0 = [0,0,8]   #水桶的初始状态
state1=[0,4,4]   #水桶最终状态
maxv = [3,5,8]    #每个水桶的对应的容积
allowed=list(itertools.permutations(range(3),2))   #1-->2,2-->1,1-->3,3-->1,2-->3,3-->2共6种可能
def nextstate(state0):    #对于状态state0，推出所有可能的下一状态
    for i,j in allowed:
        a,b=state0[i],state0[j]   # a-->b
        if a>0 and b<maxv[j]:
                nxtState = list(state0)
                if a + b > maxv[j]:     #部分倒入:a=a-(maxb-b)
                    nxtState[i] -= (maxv[j] - b)
                    nxtState[j] = maxv[j]
                else:          #a全部倒入b
                    nxtState[i] = 0
                    nxtState[j] = a+b
                yield nxtState

n=0
def findway(ways):
        global n  #多少种方法
        for state in nextstate(ways[-1]):        #遍历下一状态（ways[-1]表示最后一个状态）
                if state not in ways:         #当前状态未出现过。
                        ways.append(state)    #添加新结果
                        if state == state1:
                                n+=1
                                print('第%d种，共%d步：' %(n,len(ways)),ways)    #输出结果
                        else:
                                findway(ways)  #递归搜索
                        ways.pop()   #去除当前循环中添加的状态（回归上一级，搜索另一支线。）

findway([state0])