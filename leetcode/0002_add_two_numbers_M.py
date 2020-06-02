###
###0002. Add Two Numbers
###Runtime: 76 ms  (better than 50.17%)
###Memory Usage: 12.8 MB  (better than ?%)
###

import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    i1 = 0
    d = 1
    n = l1
    while n is not None:
        i1 = i1 + d * n.val
        d = d * 10
        n = n.next          
    i2 = 0
    d = 1
    n = l2        
    while n is not None:
        i2 = i2 + d * n.val
        d = d * 10
        n = n.next
    res_sum = str(i1 + i2)
    result_list = None
    n = None
    for c in res_sum[::-1]:
        if result_list is None:
            n = ListNode(int(c))
            result_list = n                
        else:
            n.next = ListNode(int(c))
            n = n.next            
    return result_list

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.
def test_add_243_and_564():
    result = 708

    list1 = ListNode(2)
    list1.next = ListNode(4)
    list1.next.next = ListNode(3)

    list2 = ListNode(5)
    list2.next = ListNode(6)
    list2.next.next = ListNode(4)
    

    f_result = addTwoNumbers(list1, list2)
    n = f_result
    s = ''
    while n is not None:
        s += str(n.val)
        n = n.next
    assert result == int(s)