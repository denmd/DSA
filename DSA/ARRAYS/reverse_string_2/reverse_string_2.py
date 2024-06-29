class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n=len(s)
        i=0
        new_strng=""
        while i+2*k-1<=n:
            new_strng+=s[i:i+k][::-1]+s[i+k:i+2*k]
            i+=2*k
        if n-i<k:
            new_strng+=s[i:][::-1]
        else:
            new_strng+=s[i:i+k][::-1]+s[i+k:]
        return new_strng

