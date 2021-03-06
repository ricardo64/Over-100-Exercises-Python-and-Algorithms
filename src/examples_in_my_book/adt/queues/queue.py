#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


class Queue(object):
    ''' a class for a queue '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        
    def peek(self):
        return self.items[-1]


def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.size())    
    print(queue.peek())   
    print(queue.dequeue())  
    print(queue.peek())    


if __name__ == '__main__':
    main()
