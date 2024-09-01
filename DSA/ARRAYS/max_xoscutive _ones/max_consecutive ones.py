class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        
        cnt=0
        maxs=0
        n=len(nums)
        for i in nums:
            if i==1:
                cnt+=1              
            else:
                maxs=max(maxs,cnt)
                cnt=0
        return max(maxs,cnt)