# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode.next:
        if currentNode.value != currentNode.next.value:
            currentNode = currentNode.next
        else: 
            currentNode.next = currentNode.next.next
    return linkedList

head = LinkedList(1)
head.next = LinkedList(1)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(4)
head.next.next.next.next.next.next = LinkedList(5)
head.next.next.next.next.next.next.next = LinkedList(6)
head.next.next.next.next.next.next.next.next = LinkedList(6)

removeDuplicatesFromLinkedList(head)
