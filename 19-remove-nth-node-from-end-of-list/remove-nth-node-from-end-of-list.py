# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head 
        slow = dummy 
        fast = dummy 

        # imagine a two people one at the start of the rope and other at the end of the rope with length n and start moving across a line 
        # one just crossthe line and stops .. the 2nd person is at the nth position from the end of the line right !! .. because the length of the rope is n 
        for _ in range(n+1):
            fast = fast.next 

        while fast :
            slow = slow.next 
            fast = fast.next 

        slow.next = slow.next.next 
        
        return dummy.next 