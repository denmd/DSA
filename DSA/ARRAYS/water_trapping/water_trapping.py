class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        left_max=height[0]
        right_max=height[j]
        sums=0
        while i<j:
            if left_max<=right_max:
                sums+=(left_max-height[i])
                i+=1
                left_max=max(left_max,height[i])
            else:
                sums+=(right_max-height[j])
                j-=1
                right_max=max(right_max,height[j])
        return sums