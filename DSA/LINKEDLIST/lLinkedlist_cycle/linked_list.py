class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head
        fast = head.next 
        while slow is not None and fast is not None:
            if slow == fast:
                return True
            slow = slow.next 
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
        
        return False 
        