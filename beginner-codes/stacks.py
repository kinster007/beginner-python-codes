class Stack:
    def __init__(self):
        self.stack = []
        
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return
        else:
            print("alredy in the stack.")
            
    def remove(self):
        if len(self.stack) <= 0:
            print("The stack is empty")
            return
        else:
            return self.stack.pop()
            
    def peek(self):
        return self.stack[-1]
        
stack1 = Stack()
stack1.remove()
stack1.add('007')
print(stack1.peek())
stack1.add('007')
