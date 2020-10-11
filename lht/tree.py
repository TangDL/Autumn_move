class Node():
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None
class Mytree():
    def __init__(self,root = None):
        self.root = root
    def add(self, elem):
        node = Node(elem)
        if self.root == None:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                if cur.left == None:
                    cur.left = node
                    return
                elif cur.right == None:
                    cur.right = node
                    return
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)

MyTree = Mytree()
lista = eval(input())
for i in range(len(lista)):
    MyTree.add(lista[i])


class Solution:
    def pre(self, root):
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = list()
        preorder(root)
        while -1 in res:
            res.remove(-1)
        return res
    def ino(self, root):
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = list()
        inorder(root)
        while -1 in res:
            res.remove(-1)
        return res
    def post(self, root):
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = list()
        postorder(root)
        while -1 in res:
            res.remove(-1)
        return res

test = Solution()
res = []
res.append(test.pre(MyTree.root))
res.append(test.ino(MyTree.root))
res.append(test.post(MyTree.root))
print(res)

