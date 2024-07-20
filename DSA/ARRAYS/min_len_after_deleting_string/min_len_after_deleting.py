class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        j=len(s)-1
        while i<j and s[i]==s[j]:
            while i+1<j and s[i]==s[i+1]:
                i+=1
            while i<j-1 and s[j]==s[j-1]:
                j-=1
            i+=1
            j-=1
        if i==j :
            return 1
        elif j<i:
            return 0
        else:
            return j-i+1
            // 2 pointer
            //https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/