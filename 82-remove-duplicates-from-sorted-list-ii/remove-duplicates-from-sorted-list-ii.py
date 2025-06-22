# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head 
        prev = dummy 
        curr = head 
        while curr :
            if  curr.next and curr.val == curr.next.val : # first we need to check curr.next , bc if it is None then the if statement will through error if written after the equal statement 
                while curr.next and curr.val == curr.next.val :
                    curr = curr.next 
                prev.next = curr.next # pointing new next node to the curr , bc of which duplicates gets ignored from the linkedlist 
                curr = curr.next
            else :        
                prev  = curr                    
                curr = curr.next  
        
        return dummy.next   
        