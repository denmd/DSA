# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        cur=slow.next
        while cur:
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur=next_node
        slow.next=prev
        slow=slow.next
        cur=head
        while slow:
            if cur.val!=slow.val:
                return False
            cur=cur.next
            slow=slow.next
        return True
        