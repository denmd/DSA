class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i > 0  and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]+nums[i]==0:
                    res.append([nums[j],nums[i],nums[k]])
                    j += 1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1 
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                   
                    k -= 1
                elif nums[j]+nums[k]+nums[i]<0:
                    j+=1
                else:
                    k-=1
        return res
        