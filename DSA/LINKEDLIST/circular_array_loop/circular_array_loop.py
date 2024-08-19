class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        visited_index=set()
        def getNext(index,curr_dirct):
            next_index=(index+nums[index])%n
            next_dirct=1 if nums[index]>0 else -1
            if curr_dirct!=next_dirct or index==next_index:
                return -1
            return next_index


        for i in range(n):
            if i in visited_index:
                continue
            sp,fp=i,i
            curr_dirct= 1 if nums[i]>0 else -1
            
            while True:
                sp=getNext(sp,curr_dirct)
                fp=getNext(fp,curr_dirct)
                visited_index.add(sp)
                visited_index.add(fp)

                if sp ==-1 or fp==-1:
                    break
                fp=getNext(fp,curr_dirct)
                visited_index.add(fp)
                if fp==-1:
                    break
                if sp==fp:
                    return True
        return False


        