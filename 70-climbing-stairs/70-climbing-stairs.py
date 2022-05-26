class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if(n==1):
            return 1
        
        elif(n==2):
            return 2
        
        arr = [1,2]
        
        for i in range(3,n+1):
            arr.append(arr[-1]+arr[-2])
            
        return arr[-1]
        