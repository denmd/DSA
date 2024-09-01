class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        i=0
        j=0
        n=len(s)
        maxs=0
        while j<n:
            if s[j] in d and d[s[j]]>=i:
                    i=d.get(s[j])+1 
            d[s[j]]=j
            maxs=max(maxs,j-i+1)
            j+=1
        return maxs
                
          

            
                
