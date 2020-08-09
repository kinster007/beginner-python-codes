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
    
    def search(self, key):
        if key < self.data:
            if self.left is None:
                return(str(key)) + " Not found"
            return self.left.search(key)
        elif key > self.data:
            if self.right is None:
                return(str(key)) + " Not Found"
            return self.right.search(key)
        else:
            return(str(self.data)) + " Damm yeah Found"
        
root = Node(10)

root.insert(11)
root.insert(9)
root.insert(12)
root.insert(7)
root.insert(8)
print(root.search(12))
root.printtree()
