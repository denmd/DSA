def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n=len(s)
        arr=[n+1]*n
        closest=-10
        i=0
        for i in range(n):
            if s[i]==c:
                closest=i
            if closest>=0:
                arr[i]=min(arr[i],abs(closest-i))
        closest=-10
        for i in range(n-1,-1,-1):
            if s[i]==c:
                closest=i
            if closest>=0:
                arr[i]=min(arr[i],abs(closest-i))
        return arr

        