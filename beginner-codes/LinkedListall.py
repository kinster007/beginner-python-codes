class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None
class SlinkedList:
    def __init__(self):
        self.headval = None
    
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
    def insertbegin(self, n):
        NewNode = Node(n)
        NewNode.nextval = self.headval
        self.headval = NewNode
    
    def insertend(self, m):
        NewNod = Node(m)
        if self.headval is None:
            self.headval = NewNod
            return
        temp = self.headval
        while(temp.nextval):
            temp = temp.nextval
        temp.nextval = NewNod
        
    def insertbetween(self, middle, newdata):
        if middle is None:
            print("Mentioned node is null, kindly insert")
            return
        NewNo = Node(newdata)
        NewNo.nextval = middle.nextval
        middle.nextval = NewNo
        
    def Removenode(self, removekey):
        head = self.headval
        if head is not None:
            if head.dataval == removekey:
                self.headval = head.nextval
                head = None
                return
        while head is not None:
            if head.dataval == removekey:
                break
            prev = head
            head = head.nextval
            if head is None:
                return
            prev.nextval = head.nextval
            head = None

list1 = SlinkedList()
list1.headval = Node('Jayesh')
e2 = Node('Jain')
e3 = Node('theZ')

list1.headval.nextval = e2
e2.nextval = e3

list1.insertbegin('007')

list1.insertend('007')

list1.insertbetween(list1.headval.nextval.nextval, '008')

list1.Removenode('008')

list1.listprint()
