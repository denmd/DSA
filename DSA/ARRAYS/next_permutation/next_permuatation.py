class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)-1
        i=n-1
        ind1=-1
        for i in range(n-1,-1,-1):
            if nums[i]<nums[i+1]:
                ind1=i
                break
        if ind1 == -1:
            return nums.sort()
        ind2=-1
        for i in range(n,ind1,-1):
            if nums[i]>nums[ind1]:
                ind2=i
                break
        nums[ind1],nums[ind2]=nums[ind2],nums[ind1]
        nums[ind1+1:] = nums[ind1+1:][::-1]
      