class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        score=0
        i=-1
        j=len(tokens)
        tokens.sort()
        max_score=0
        while i<j:
            if i+1<j and tokens[i+1]<=power:
                score+=1
                max_score=max(max_score,score)
                i+=1
                power-=tokens[i]
            elif i<j-1 and score >=1:
                j-=1
                score-=1
                power+=tokens[j]
            else:
                return max_score
        return max_score
                
        