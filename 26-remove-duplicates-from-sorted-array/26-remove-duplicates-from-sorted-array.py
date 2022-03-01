class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(nums==[]):
            return []
        
        prev = nums[0]
        count = 1 
        i = 1 
        a = len(nums) 
        
        while(i<len(nums)):       
            
            if(nums[i]==prev):
                nums.pop(i)
                i = i-1
                
            else:
                count = count+1 
                prev = nums[i]
            
            i = i+1 
            
        
                        
        return count