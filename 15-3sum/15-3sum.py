class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        nums.sort()
        
        
        output = []
        
        for i in range(len(nums)):
            
            
            if(i==0 or (nums[i-1]!=nums[i])):
                left = i+1 
                right = len(nums)-1
                
    
                
                while(left<=len(nums)-1 and left<right):
                    
                 
                
                        
                    if(nums[left]+nums[right]==0-nums[i]):
                        
                        output.append([nums[i],nums[left],nums[right]])
                        left = left+1
                        right = right-1 
                        
                        
                        while(left<len(nums) and nums[left]==nums[left-1]):
                            left = left+1 
                            
                        
                    elif(nums[left]+nums[right]>0-nums[i]):
                        right = right-1
                        
                    else:
                        left = left+1 
                    
                
        return output 
     
                        
                        
        
        
        
        
                