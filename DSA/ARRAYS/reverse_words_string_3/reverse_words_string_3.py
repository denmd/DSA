class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s= s[::-1]
        words=s.split()
        words.reverse()
        s=' '.join(words)
        return s
        

        https://leetcode.com/problems/reverse-words-in-a-string-iii/    