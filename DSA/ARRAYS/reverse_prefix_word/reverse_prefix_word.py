class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ind=-1
        for i in range(len(word)):
            if word[i]==ch:
                ind=i
                break
        if ind!=-1:
            word=word[:ind+1][::-1]+word[ind+1:]
        return word
        

or


USE ind=word.find(ch)  //return 1 st occurecane else -1


