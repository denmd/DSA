class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        brk_pnt1=-1
        digits=[int(digit) for digit in str(n)]
        for i in range(len(digits)-1-1,-1,-1):
            if digits[i]<digits[i+1]:
                brk_pnt1=i
                break
        if brk_pnt1==-1:
            return -1
        for i in range(len(digits)-1,brk_pnt1,-1):
            if digits[i]>digits[brk_pnt1]:
                brk_pnt2=i
                break
        digits[brk_pnt1], digits[brk_pnt2]=digits[brk_pnt2],digits[brk_pnt1]
        digits[brk_pnt1+1:]=digits[brk_pnt1+1:][::-1]
        n=int(''.join(map(str,digits)))
        if n > 2**31-1:
            return -1
        return n
      

        