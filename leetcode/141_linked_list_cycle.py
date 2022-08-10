# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        
        fast = head.next
        slow = head
        while fast and fast.next:
            try:
                if fast == slow:
                    return True
                fast = fast.next.next
                slow = slow.next
            except:
                return False
            
        return False