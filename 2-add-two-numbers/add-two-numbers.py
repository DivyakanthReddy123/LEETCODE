# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # curr1 = l1 
        # curr2 = l2 
        # n1 = ''
        # n2 = ''
        # while curr1 :
        #     n1 += str(curr1.val)
        #     curr1  =curr1.next 
        
        # while curr2 :
        #     n2 += str(curr2.val)
        #     curr2 = curr2.next 
        
        # finalSum = int(n1[::-1]) + int(n2[::-1])

        # def appendList( val):
        #     newNode = ListNode(val)
        #     if not head :
        #         head = newNode 

        #     curr = head 

        #     while curr.next :
        #         curr = curr.next 

        #     curr.next = newNode 

        # def printList(self):
        #     curr = head 
        #     while curr : 
        #         # print(curr.val, end="->")
        #         curr = curr.next 
        #     return head 

        # curr = head 

        # for n in str(finalSum)[:-1] :
        #     curr = appendList(n)

        # return curr 
        curr1 = l1 
        curr2 = l2 
        n1 = ''
        n2 = ''

        # Build number strings
        while curr1:
            n1 += str(curr1.val)
            curr1 = curr1.next
        
        while curr2:
            n2 += str(curr2.val)
            curr2 = curr2.next
        
        # Reverse strings, add, reverse result
        total = str(int(n1[::-1]) + int(n2[::-1]))[::-1]

        # Build new linked list from total
        head = ListNode(int(total[0]))
        curr = head
        for digit in total[1:]:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return head