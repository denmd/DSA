class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
     
        i=0
        j=len(nums)-1
        nums.sort()
        maxs=0
        while i<j:
            if maxs < nums[j]+nums[i]:
                maxs=nums[i]+nums[j]
            j-=1
            i+=1
        return maxs