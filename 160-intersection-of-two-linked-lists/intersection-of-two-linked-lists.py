# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curr1 = headA
        curr2 = headB 
        nod = set()
        while curr1  :
            if curr1 not in nod :
                nod.add(curr1)
            curr1 = curr1.next 
        while curr2 :
            if curr2 in nod :
                return curr2
            curr2 = curr2.next
        return None       