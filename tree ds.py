class Node:
    def _init_(self,data):
        self.right=None
        self.left=None
        self.data=data
    def printTree(self):
        print(self.data)
root=Node(12)
root.printTree()