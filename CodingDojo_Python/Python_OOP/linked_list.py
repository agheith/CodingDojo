# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class SinglyLinkedList(object):
#     def __init__(self):
#         self.head = None
#         self.tail = None
# #
# # list = SinglyLinkedList()
# # list.head = Node('Alice')
# # list.head.next = Node('Chad')
# # list.head.next.next = Node('Debra')
# # print head.next.next.value
#
# list = SinglyLinkedList()
# list.head = Node('Alice')
# list.head.next = Node('Chad')
# list.head.next.next = Node('Debra')
# # something close to this should be utilized for all of the above problems
# runner = list.head
# while(runner.next != None):
#     print(runner.val)
#     runner = runner.next

#
# class Node(object):
#
#     def __init__(self,value):
#
#         self.value = value
#         self.nextnode = None
#
# a = Node(1)
# b = Node(2)
# c = Node(3)
#
# a.nextnode = b
# b.nextnode = c
#
# print a.nextnode.value, b.nextnode.value

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = linked_list.head
        while node:
            yield node
            node = node.next

    def add(self, node):
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def reverse(head):
        current = head
        previous = None
        next = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

    
linked_list = SinglyLinkedList()
linked_list.add(Node('Alice'))
linked_list.add(Node('Ben'))
linked_list.add(Node('Chad'))
linked_list.add(Node('Debra'))

# print [previous.value for node in linked_list]
print [node.value for node in linked_list]  # ['Alice', 'Chad', 'Debra']
