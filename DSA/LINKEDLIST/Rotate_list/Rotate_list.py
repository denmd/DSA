# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k==0:
            return head
        cur=head
        n=1
        while cur.next:
            n+=1
            cur=cur.next
        k=k%n
        if(k==0):
            return head
        cur.next=head
        temp=head
        for _ in range(1,n-k):
            temp=temp.next
        newhead=temp.next
        temp.next=None
        return newhead

        