class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        
        nums.sort()
        
        
        
        output = []
        
        
        for i,a in enumerate(nums):
            if(i==0 or (nums[i]!=nums[i-1]) ):
                
                if(i+3<len(nums)):
                    j = i+1
                      
                    while(j<=len(nums)-3):
                        
                        while(j<len(nums) and nums[j-1]==nums[j] and j!=i+1):
                            j=j+1
                        
                        left = j+1 
                        right = len(nums)-1
                        
                        while(left<right):
                           
                            
                            if(a+nums[j]+nums[left]+nums[right])==target:
                                output.append([a,nums[j],nums[left],nums[right]])
                                left = left+1
                                
                                while(left<len(nums) and nums[left]==nums[left-1]):
                                    left=left+1
                                    
                                    
                            elif(a+nums[j]+nums[left]+nums[right])>target:
                                right=right-1
                                
                            elif(a+nums[j]+nums[left]+nums[right])<target:
                                left = left+1
                         
                        j=j+1
                        
                            
        return(output)
                
                                
            