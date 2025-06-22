# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        # now by comparing that nodes value to other nodes we build two linkedlist 
        
        if head == None :
            return head 

        dummy = ListNode(-1)
        list1 = dummy
        dummy2  = ListNode(-1)
        list2 = dummy2

        curr1 = head 
        while  curr1 :
            if curr1.val < x :
                list1.next =  curr1 
                list1 = list1.next
            else :
                list2.next = curr1
                list2 = list2.next 
            curr1 =curr1.next    

        list2.next = None 
        list1.next =  dummy2.next# i dont know how to add head of the list2 linkedlist here ? ?
        
        return dummy.next 