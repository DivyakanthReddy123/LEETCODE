# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head 
        slow = dummy 
        fast = dummy 
        curr = head 
        n = 0

        if not head or not head.next or k == 0:
            return head


        while curr : 
            curr = curr.next 
            n+=1  


        if k == n :
            return head 
        
        k = k%n 
      
        if k == 0 :
            return head 

        for _ in range(k):
            if fast.next :  
                fast = fast.next 
        
        while fast.next :
            fast = fast.next 
            slow = slow.next 

        
        new_head = slow.next # new node 4 
        fast.next = head 
        slow.next = None 
        
        return new_head 