class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    count = 0
    currentNode = linkedList
    while currentNode:
        count = count + 1
        currentNode = currentNode.next

    middleNode = linkedList
    for _ in range(count // 2):
        middleNode = middleNode.next
    return middleNode


def middleNode2(linkedList):
    slowNode = linkedList
    fastNode = linkedList

    while fastNode and fastNode.next:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    return slowNode


head = LinkedList(1)
head.next = LinkedList(1)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(4)
middleNode(head)

"""
result = middleNode(head)
print(result.value)
"""
