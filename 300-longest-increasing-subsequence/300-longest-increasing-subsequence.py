class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        # [3,1,4]
        
        # [3,] [1,4] 
        
        # [1,3,2,4]
        arr = [0 for i in range(len(nums))] 
        # recursive solution 
        arr[0]=1
        
        for i in range(1,len(nums)):
            j = (len(nums)-1-i)
            max_seq = 1 
            
            for k in range(0,i):
                if(nums[len(nums)-1-k]>nums[len(nums)-1-i]):
                    max_seq = max(max_seq,arr[k]+1)
            arr[i]=max_seq
            
     
            
        return max(arr)
            
            
        
            
        
        