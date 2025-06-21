# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        curr1 = l1 
        curr2 = l2 
        n1 = ''
        n2 = ''
        while curr1 :
            n1 += str(curr1.val)
            curr1  =curr1.next 
        
        while curr2 :
            n2 += str(curr2.val)
            curr2 = curr2.next 
        
        finalSum = str ( int(n1[::-1]) + int(n2[::-1]) )[::-1]
        head = ListNode(int(finalSum[0]))
        curr = head 

        for i in finalSum[1:]:
            curr.next = ListNode(int(i))
            curr = curr.next 

        return head 
        