# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        curr = dummy 
        

        # this is just to add the first value into the FINAL LINKEDLIST ( head node )
        # we can directly do this below instead of curr.next = ListNode(curr1.val) or curr2.val 
        # because this takes to much space !! 

        # use AND here not or , because when one traversing one linkedlist is done then curr1.next
        # curr2.next will through error 
        while list1 and list2 :
            if list1.val <= list2.val :
                curr.next = list1
                list1 = list1.next
            else :
                curr.next = list2
                list2 = list2.next
            curr = curr.next 

        # add the remaining NODEs of LINKEDLIST to the final LINKEDLIST 
        curr.next = list1 if list1 else list2
           
        return dummy.next   

        