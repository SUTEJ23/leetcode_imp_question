class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gap = []
        s = 0
        e = 0
       
        for i in range(len(startTime)):
          
            if i-1>=0:
                e = endTime[i-1]
            s = startTime[i]
            gap.append(s-e)
        if eventTime != endTime[-1]:
            gap.append(eventTime-endTime[-1])
        l = 0 
        r = 1
        ans = gap[0]
        res =ans
        print(gap)
        while l<=r and r<len(gap):
            if r-l+1<=k+1:
                res = res + gap[r]
            else:
                res = res - gap[l]+gap[r]
                l+=1    
            ans = max(ans,res) 
            r+=1
        return ans    

                

        
        