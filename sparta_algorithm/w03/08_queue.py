class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # head    tail
    # [4]  ->  [2]
    # new_node = Node(3) # [3]추가
    #
    # head    tail
    # [4]  ->  [2]  ->  [3]
    # self.tail.next = new_node
    # head             tail
    # [4]  ->  [2]  ->  [3]
    # self.tail = new_node

    def enqueue(self, value):
        new_node = Node(value)  # [3]
        if self.is_empty():  # 만약 비어있다면,
            self.head = new_node  # head 에 new_node를
            self.tail = new_node  # tail 에 new_node를 넣어준다.
            return

        self.tail.next = new_node
        self.tail = new_node

    # head             tail
    # [4]  ->  [2]  ->  [3]
    # delete_head = self.head
    #
    # self.head = self.head.next
    #          head    tail
    # [4]  ->  [2]  ->  [3]
    #
    # return delete_head
    # head    tail
    # [2]  ->  [3]    반환 [4]

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"  # 만약 비어있다면 에러!

        delete_head = self.head  # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next  # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.

        return delete_head.data  # node로 반환하면 보기 힘들기 때문에 .data로 반환

    def peek(self):
        if self.is_empty():
            return "Queue is empty!"

        return self.head.data

    def is_empty(self):
        return self.head is None


queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())



