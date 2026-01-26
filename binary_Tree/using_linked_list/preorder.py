class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

binaryTree=TreeNode("drinks")
leftchild=TreeNode("hot")
rightchild=TreeNode("cold")
binaryTree.leftchild=leftchild
binaryTree.rightchild=rightchild

def preorder(rootnode):
    if not rootnode:
        return
    else:
        print(rootnode.data)
        preorder(rootnode.leftchild)
        preorder(rootnode.rightchild)

preorder(rootnode=binaryTree)
