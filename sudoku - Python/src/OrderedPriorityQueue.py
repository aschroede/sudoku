import queue
from itertools import count


class OrderedPriorityQueue:
    def __init__(self):
        self.priority_queue = queue.PriorityQueue()
        self.counter = count()
        self.queue = self.priority_queue.queue

    def put(self, item):
        priority = next(self.counter)
        self.priority_queue.put((priority, item))

    def get(self):
        priority, item = self.priority_queue.get()
        return item

    def empty(self):
        return self.priority_queue.empty()



