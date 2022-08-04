# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        m = 0
        n = 0
        temp = headA
        while temp != None:
            m+=1
            temp = temp.next
        temp = headB
        while temp != None:
            n+=1
            temp = temp.next
        diff = 0
        if m>=n : 
            diff = m-n
        else:
            diff = n-m
        p1 = headA
        p2 = headB
        if max(m,n) == m:
            while diff > 0:
                p1 = p1.next
                diff-=1
        else:
            while diff > 0:
                p2 = p2.next
                diff-=1
        while p1 != None and p2!=None:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None