class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        i=0
        j=len(s)
        res=[]
        for x in s:
            if x=='I':
                res.append(i)
                i+=1
            else:
                res.append(j)
                j-=1

        res.append(i)
        return res
