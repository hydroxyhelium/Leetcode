class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        if(nums==[]):
            return 0 
        
        i = 0 
        count = 0 
        
        while(i<len(nums)):
            if (nums[i])==val:
                nums.pop(i)
                i=i-1
                
            else:
                count= count+1 
            i = i+1 
        
        return count