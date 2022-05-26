class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        # [1,2,3,1]
        
        # [1]:1, [2]:1, [3]:1
        
        hashset=set()
        
        for i in nums:
            if i in hashset:
                return True
            
            hashset.add(i)
            
        return False 
            
            