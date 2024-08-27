class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        n=len(nums)
        cnt_all=0
        cnt_small=0
        i=0
        j=0
        maxs=0
        while j<n:
           if nums[j]<=right :
                   cnt_all+= (j-i)+1
           else:
                i=j+1
           j+=1
        i=0 
        j=i 
        while j<n:
            if nums[j] <=left-1:
                cnt_small += (j-i)+1
            else:
                i=j+1
            j+=1
        return (cnt_all-cnt_small)


        



        
            
        