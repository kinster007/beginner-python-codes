class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data, end = " ")
        if self.right:
            self.right.printtree()
            
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        
root = Node(10)

root.insert(11)
root.insert(9)
root.insert(12)
root.insert(7)
root.insert(8)

root.printtree()
