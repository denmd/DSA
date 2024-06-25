class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1
        cnt=0
        def checksubarrayvalid(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        while i<=j:
            if s[i]!=s[j]:   
               return checksubarrayvalid(i+1,j) or checksubarrayvalid(i,j-1)

            i+=1
            j-=1
        
        return True