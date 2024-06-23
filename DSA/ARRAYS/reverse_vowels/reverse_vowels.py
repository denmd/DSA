class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        j=len(s)-1
        vo=["a","e","i","o","u","A","E","I","O","U"]
        s=list(s)
        while i<j:
            if s[i] in vo and s[j] in vo:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] not in vo:
                i+=1
            else:
                j-=1
        s=''.join(map(str,s))
        return s
        
        