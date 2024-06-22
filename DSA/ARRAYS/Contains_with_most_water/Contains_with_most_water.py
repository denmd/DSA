class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        max_water=0
        while i < j:
            if height[i]<=height[j]:
                max_water=max(max_water,(j-i)*height[i])
                i+=1
            else:
                max_water=max(max_water,(j-i)*height[j])
                j-=1
        return max_water
        