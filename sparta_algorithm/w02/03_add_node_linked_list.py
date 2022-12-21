class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, data):
        new_node = Node(data) # 새로운 노드 추가 [6]
        if index == 0:
            new_node.next = self.head # [6] -> [5]
            self.head = new_node # heda ->
            return
        node = self.get_node(index -1) # 앞쪽 노드 변수로 저장 [5]
        next_node = node.next # 뒤쪽 노드 임시저장 [12]
        node.next = new_node # [5] -> [6]
        new_node.next = next_node # [6] -> [12]

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(1, 6) # 5와 12 사이에 6 추가하기 (넣을자리, 넣을것)
linked_list.print_all()
    # def add_node(self, index, value):
    #     new_node = Node(value)
    #     if index == 0:
    #         new_node.next = self.head
    #         self.head = new_node
    #         return
    #
    #     node = self.get_node(index - 1)
    #     next_node = node.next
    #     node.next = new_node
    #     new_node.next = next_node
    #
    # def delete_node(self, index):
    #     if index == 0:
    #         self.head = self.head.next
    #         return
    #     node = self.get_node(index - 1)
    #     node.next = node.next.next


# linked_list = LinkedList(3)
# linked_list.append(4)
# linked_list.append(5)
# linked_list.add_node(0, 3)
# linked_list.print_all()