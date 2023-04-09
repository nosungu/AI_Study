class ListQueue:
    def __init__(self):
        self.__queue = []
        
    def enqueue(self,x):
        self.__queue.append(x)

    def dequeue(self):
        self.__queue.pop(0)
    
    def front(self):
        self.__queue.get(0) 

    def isEmpty(self):
        if not self.__queue():
            return self.isEmpty()

    def dequeueAll(self):
        self.__queue.clear()

    def printQueue(self):
        print(self.__queue)

        
q1 = ListQueue()
q1.enqueue("Mon")
q1.enqueue("Tue")
q1.enqueue(1234)
q1.enqueue("Wed")
q1.dequeue()
q1.enqueue('aaa')
q1.printQueue()

