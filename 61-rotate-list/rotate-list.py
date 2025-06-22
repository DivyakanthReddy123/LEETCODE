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

        # this problem is similar to the remove nth node from the linkedlist !! 
        # but here we are doing k%n because k might be large than n also 
        # but here we go till the last node not further above it to the None as in the prev problem
        if not head or not head.next or k == 0:
            return head

        # to count the number of Nodes in the LINKEDLIST 
        while curr : 
            curr = curr.next 
            n+=1  

        # when this is the case we get the same linkedlist if after rotating it 
        if k == n :
            return head 
        
        k = k%n 
      
        if k == 0 :
            return head 

        for _ in range(k):
            if fast.next :  
                fast = fast.next 
        
        # but here we go till the last node not further above it to the None as in the prev problem
        while fast.next :
            fast = fast.next 
            slow = slow.next 

        
        new_head = slow.next # just to save the START POINT of the new LINKEDLIST  
        fast.next = head  # point the last node in the previous LINKEDLIST to the head of the new LINKEDLIST 
        slow.next = None 
        
        return new_head 