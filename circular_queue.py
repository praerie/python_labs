class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity  # fixed-size list to store elements
        self.capacity = capacity        # max number of items allowed
        self.front = 0                  # index to dequeue from
        self.rear = 0                   # index to enqueue to
        self.count = 0                  # current number of items

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
        print(f"Enqueued: {item} | Queue: {self.queue}")

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None  
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"Dequeued: {item} | Queue: {self.queue}")
        return item

    def is_empty(self):
        empty = self.count == 0
        print(f"is_empty(): {empty}")
        return empty

    def is_full(self):
        full = self.count == self.capacity
        print(f"is_full(): {full}")
        return full

    def size(self):
        print(f"size(): {self.count}")
        return self.count

if __name__ == "__main__":
    q = CircularQueue(3)

    # check initial state
    q.is_empty()
    q.is_full()
    q.size()

    # enqueue 3 elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    # queue should be full now
    q.is_full()
    q.size()

    # dequeue 1 element
    q.dequeue()

    # queue should NOT be full now
    q.is_full()
    q.is_empty()
    q.size()

    # enqueue another item to test wrap-around
    q.enqueue(40)

    # final dequeues
    while not q.is_empty():
        q.dequeue()
    
    # final state check
    q.is_empty()
    q.size()
