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
            self.queue.pop()
            return
        return ("queue is empty")
        
    def printq(self):
        print(self.queue)
        
TheQueue = Queue()
TheQueue.add("Mon")
TheQueue.add("Tue")
TheQueue.add("Wed")
TheQueue.printq()
TheQueue.remove()
TheQueue.printq()
