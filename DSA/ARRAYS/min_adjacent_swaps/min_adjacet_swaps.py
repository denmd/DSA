class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        cnt=0
        old_num=num
        while k!=0:
            lst_num=list(num)
            ind1=-1
            for i in range(len(lst_num)-1-1,-1,-1):
                if lst_num[i]<lst_num[i+1]:
                    ind1=i
                    break;
            for i in range(len(lst_num)-1,ind1,-1):
                if lst_num[i]>lst_num[ind1]:
                    ind2=i
                    break
            lst_num[ind1],lst_num[ind2]= lst_num[ind2] , lst_num[ind1]
            lst_num[ind1+1:]=lst_num[ind1+1:][::-1]
            num= ''.join(map(str,lst_num))
            k-=1
        
        new_num=list(num)
        old_num=list(old_num)
        # for i in range(len(num)-1,-1,-1):
        #     if old_num[i]!=num[i]:
        #         last_change=i
        for i in range(len(old_num)-1):
            if old_num[i] !=new_num[i]:
                j=i
                while old_num[i]!=new_num[j]:
                    j+=1
                while j>i:
                    new_num[j],new_num[j-1]=new_num[j-1],new_num[j]
                    cnt+=1
                    j-=1
        return cnt
                   
                 
                
                    
    
            

        