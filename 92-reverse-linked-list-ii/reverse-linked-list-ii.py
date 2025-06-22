# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy = ListNode(-1)
        dummy.next = head 
        curr = dummy
        pos = 0

        # this is to assign the lRem before entering the internal linkedlist 
        # we stop curr right before the start internal linkedlist 
        while pos < left - 1 :
            curr = curr.next 
            pos += 1 

        lRem = curr 
        start = curr.next 

        # lRem is before the start of the internal linkedlist 
        # prev ends at the internal linkedlist 
        # use start as the start for the internal linkedlist 
        
        # now start reversing the linkedlist 
        prev = curr.next # prev is at the start of the internal linkedlist 
        curr = curr.next # curr is at the 2nd of the internal linkedlist 
        for _ in range(right-left+1): # the + 1 gets ignored because of the range here 
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 

        lRem.next = prev 
        start.next = curr 

        return dummy.next         
        