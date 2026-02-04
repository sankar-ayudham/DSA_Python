class BSTree:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def insert(rootNode, value):
    if rootNode.data is None:
        rootNode.data = value
    elif value <= rootNode.data:
        if rootNode.leftNode is None:
            rootNode.leftNode = BSTree(value)
        else:
            insert(rootNode.leftNode, value)
    else:
        if rootNode.rightNode is None:
            rootNode.rightNode = BSTree(value)
        else:
            insert(rootNode.rightNode, value)
    return 'node successfully inserted'

def postorder(rootNode):
    if not rootNode:
        return "there is nothing or nothing reamining"
    else:
        postorder(rootNode.leftNode)
        postorder(rootNode.rightNode)
        print(rootNode.data)


BST = BSTree(None)
insert(BST, 70)
insert(BST, 50)
insert(BST, 90)
insert(BST, 30)
insert(BST, 80)
insert(BST, 100)
insert(BST, 20)
insert(BST, 40)
postorder(BST)



