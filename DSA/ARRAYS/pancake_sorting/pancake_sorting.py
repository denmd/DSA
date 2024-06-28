class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        j=len(arr)
        max_element=1
        max_ind=0
        res=[]
        while j>1: 
            max_ind=arr.index(max(arr[:j]))
            if max_ind==j-1:
                j-=1
                continue
            if max_ind==0:
                arr[:j]=arr[:j][::-1]
                res.append(j)
                j-=1
                continue
            arr[:max_ind+1]=arr[:max_ind+1][::-1]
            res.append(max_ind+1)
            arr[:j]=arr[:j][::-1]
            res.append(j)
            j-=1
        return res



