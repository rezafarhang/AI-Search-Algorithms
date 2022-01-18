class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, node):
        self.queue.append(node)

    def dequeue(self):
        node = self.queue[0]
        self.queue.__delitem__(0)
        return node

    def isempty(self):
        if len(self.queue) == 0:
            return 1
        return 0

    def state_exist(self, state):
        if state in self.queue:
            return 1
        return 0

    def get_queue(self):
        return self.queue