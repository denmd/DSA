class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        j=1
        n=len(nums)
        while i<n-1 and j<n:                       //O(n)
            if nums[i]%2==0 and nums[j]%2!=0:
                i+=2
                j+=2
                continue
            while i<n-1 and nums[i]%2==0:          //O(n/2)
                i+=2
            while j<n and nums[j]%2!=0:            // O(n/2)
                j+=2
            nums[i],nums[j]=nums[j],nums[i]
        return nums
        https://leetcode.com/problems/sort-array-by-parity-ii/