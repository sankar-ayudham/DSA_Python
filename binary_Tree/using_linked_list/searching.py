import myqueue
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



def searchBT(rootnode , nodevalue):
    if not rootnode:
        return
    else:
        custom_quque= myqueue.Queue()
        custom_quque.enqueue(rootnode)
        while not custom_quque.isEmpty():
            root= custom_quque.dequeue()
            # print(root.value.data)
            if root.value.data == nodevalue:
                return "success"
            if root.value.leftchild is not None:
                custom_quque.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                custom_quque.enqueue(root.value.rightchild)
        return "not found"

print(searchBT(binaryTree,"cold"))