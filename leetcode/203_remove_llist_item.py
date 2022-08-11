# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        while head and head.val==val:
            head = head.next
        if not head:
            return None            
        original_head = head
        while head.next:
            if head.next.val==val:
                head.next = head.next.next
            else:
                head = head.next
        return original_head

            