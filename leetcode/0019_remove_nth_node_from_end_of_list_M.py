###
###19. Remove Nth Node From End of List
###Runtime: 40 ms, faster than 49.46% of Python3 online submissions for Remove Nth Node From End of List.
###Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.
###

import pytest

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    arr = []
    node = head
    while node != None:
        arr.append(node)
        node = node.next
    if len(arr) == 1:
        return None
    x = len(arr) - n
    if x == 0:
        head = arr[1]
    elif n == 1:            
        arr[len(arr)-2].next = None
    else:
        arr[x - 1].next = arr[x + 1]
    return head


#Given linked list: 1->2->3->4->5, and n = 2.
#After removing the second node from the end, the linked list becomes 1->2->3->5.
def test_12345_n2():
    n = 2
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(4)
    list.next.next.next.next = ListNode(5)

    result = '1235'
    f_result = removeNthFromEnd(list, n)
    s = ''
    node = f_result
    while node is not None:
        s += str(node.val)
        node = node.next

    assert result == s


def test_1_n1():
    n = 1
    list = ListNode(1)

    result = ''
    f_result = removeNthFromEnd(list, n)
    s = ''
    node = f_result
    while node is not None:
        s += str(node.val)
        node = node.next

    assert result == s