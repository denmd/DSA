class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        j=len(s)-1
        s=list(s)
        while i<j:
            if  s[i].isalpha() and  s[j].isalpha():
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            if not s[i].isalpha() :
                i+=1
            if not  s[j].isalpha():
                j-=1
            
        s=''.join(map(str,s))
        return s
        //2 pointer