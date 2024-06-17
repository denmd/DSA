class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        j=len(nums)-1
        cnt=0
        nums.sort()
        mod=10**9 + 7
        while i<=j:
            if  nums[i]+nums[j]>target:
                j-=1
            else:
                cnt+=pow(2,j-i,mod)
                i+=1
        return cnt % mod

        