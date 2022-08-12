# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        cur = head
        prev = None
        while cur:
                next_c = cur.next
                cur.next = prev
                prev = cur
                cur = next_c
        return prev