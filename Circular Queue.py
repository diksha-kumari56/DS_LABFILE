MAX_SIZE = 100  

class CircularQueue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.arr = [0] * MAX_SIZE

    def is_full(self):
        if (self.front == 0 and self.rear == MAX_SIZE - 1) or \
           (self.rear == (self.front - 1) % (MAX_SIZE - 1)):
            return True
        return False

    def is_empty(self):
        return self.front == -1

    def enQueue(self, value):
        if self.is_full():
            print("Queue is full.")
        else:
            if self.front == -1:
                self.front = 0

            self.rear = (self.rear + 1) % MAX_SIZE
            self.arr[self.rear] = value
            print(f"Enqueued element: {value}")

    def deQueue(self):
        if self.is_empty():
            print("Queue is empty.")
            return -1

        element = self.arr[self.front]

        if self.front == self.rear:

            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % MAX_SIZE

        print(f"Dequeued element: {element}")
        return element

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Elements in the queue:", end=" ")

        i = self.front
        while i != self.rear:
            print(self.arr[i], end=" ")
            i = (i + 1) % MAX_SIZE

        print(self.arr[i])   

if __name__ == "__main__":
    q = CircularQueue()

    q.enQueue(10)
    q.enQueue(20)
    q.enQueue(30)
    q.enQueue(40)

    q.display()

    q.deQueue()
    q.deQueue()

    q.display()

    q.enQueue(50)
    q.enQueue(60)

    q.display()
