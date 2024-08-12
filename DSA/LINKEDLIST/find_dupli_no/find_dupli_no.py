class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow


        or



        class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sets=set()
        for i in nums:
            if i in sets:
                return i
            else:
                sets.add(i)