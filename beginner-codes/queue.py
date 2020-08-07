class Queue:
    def __init__(self):
        self.queue = list()
    
    def add(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return
        return ("Already in the queue")
    
    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("queue is empty")
        
TheQueue = Queue()
TheQueue.add("Mon")
TheQueue.add("Tue")
TheQueue.add("Wed")
print(TheQueue.remove())
print(TheQueue.remove())
