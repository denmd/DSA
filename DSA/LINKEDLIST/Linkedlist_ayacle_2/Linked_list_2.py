class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
           return None
        slow=head
        fast=head
        while fast and fast.next:
          slow=slow.next
          fast=fast.next.next
          if slow==fast:
            break
          
        if not fast or not fast.next:
            return None
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
        