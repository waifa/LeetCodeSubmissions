# link: https://leetcode.com/problems/add-two-numbers/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        ret = l3
        carryover = 0
        while l1 != None or l2 != None:
            if l1 == None:
                l1 = ListNode(0)
            elif l2 == None:
                l2 = ListNode(0)
                
            if (l1.val + l2.val + carryover) >= 10:
                l3.val = l1.val + l2.val - 10 + carryover
                carryover = 1
            else:
                l3.val = l1.val + l2.val + carryover
                carryover = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2:
                l3.next = ListNode()
                l3 = l3.next
        if carryover:
            l3.next = ListNode(1)
            
        return ret