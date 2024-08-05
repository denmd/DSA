def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        start=0
        end=len(arr)-1
        while start<=end:
            mid=(start+end)//2
            if arr[mid]>x:
                end=mid-1
            elif arr[mid]<x:
                start=mid+1
            else:
                break
        
        if start>end:
            mid=end
        i=mid
        j=mid+1
        res=[]
        while len(res)<k:
            if i>=0 and j<len(arr):
                if abs(arr[i]-x)<abs(arr[j]-x):
                    res.append(arr[i])
                    i-=1
                elif  abs(arr[i]-x)==abs(arr[j]-x) and i<j:
                      res.append(arr[i])
                      i-=1
                else:
                    res.append(arr[j])
                    j+=1
            elif i>=0:
                res.append(arr[i])
                i-=1
            elif j<len(arr):
                res.append(arr[j])
                j+=1
        res.sort()
        return res

    