class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def mergeTwoLists(l1,l2):
    if not l1 and not l2:
        return []
    if not l1:
        return l2
    if not l2:
        return l1

    dummy = Node(-1)
    curr = dummy

    a = l1
    b = l2
    while a and b:
        if a.value < b.value:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next
        curr = curr.next
    if a:
        curr.next = a
    if b:
        curr.next = b
    return dummy.next
