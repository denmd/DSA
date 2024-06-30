class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word=""
        s_list=[]
        new_string=''
        space=0
        for char in s:
            if char!= " ":
                word+=char
                space=0
            elif  space!=1:
                s_list.append(word)
                word=""
                space=1
        s_list.append(word)
        for i in range(len(s_list)-1,0,-1):
            if s_list[i]!="":
                new_string+=s_list[i]
                if s_list[i-1]!="":
                    new_string+=" "
        
        new_string+=s_list[0]
        return new_string


       
        or

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wordAndSpaces = s.split()
        result = ''
        wordAndSpaces.reverse()
        result = ' '.join(wordAndSpaces)

        return result