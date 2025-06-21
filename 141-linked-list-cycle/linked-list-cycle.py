# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # ele = set()
        # curr = head 
        # while curr :
        #     if curr in ele : # dont check for the val in set .. check for the node if it is in the set .. there might be nodes with same values 
        #         return True 
        #     else : 
        #         ele.add(curr)
  
        #     curr = curr.next 
        # print(ele)
        # return False 

    # another approach take two pointers .. one takes one jump at a time 
    # another takes two jumps at a time .. if cycle exists then both will 
    # end up at one NODE some point in time 
        slow = fast = head 
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next
            if slow == fast : 
                return True 
        return False 
            