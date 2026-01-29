class BinaryTree:
    def __init__(self,size):
        self.list=size*[None]
        self.lastUsedindex=0
        self.maxsize=size

    def insert(self,value):
        if self.lastUsedindex+1==self.maxsize:
            return "the binary treee is full"
        self.list[self.lastUsedindex+1]=value
        self.lastUsedindex +=1
        return "inserted successfully"
    def levelorder(self,index):
        for i in range(index,self.lastUsedindex+1):
            print(self.list[i])

    def deleteNode(self,value):
        if self.lastUsedindex==0:
            return "there are no elements to delete"
        for i in range(1,self.lastUsedindex+1):
            if self.list[i]==value:
                self.list[i]=self.list[self.lastUsedindex]
                self.list[self.lastUsedindex]=None
                self.lastUsedindex-=1
                return "element successfully deleted"

BTree= BinaryTree(6)
BTree.insert("drinks")
BTree.insert("hot")
BTree.insert("cold")
BTree.insert("tea")
BTree.insert("coffee")

BTree.deleteNode("coffee")
BTree.levelorder(1)
