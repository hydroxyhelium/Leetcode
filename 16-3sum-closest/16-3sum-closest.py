class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        output = [99999999999999999999999,0]
        
        nums.sort() 
        
        for i,a in enumerate(nums):
            if(i==0 or (nums[i]!=nums[i-1])):
                left = i+1
                right = len(nums)-1 
                
                
                while(left<right):
                    
                    if abs(target-(nums[left]+nums[right]+a))< output[0]:
                            output[0]= abs(target-(nums[left]+nums[right]+a))
                            output[1] = [a,nums[left],nums[right]]
                    
                    if (target-(nums[left]+nums[right]+a))>=0:
                        
                        left = left+1 
                    
                    elif (target-(nums[left]+nums[right]+a))<0:
                        right = right-1 
                    
                
        return(sum(output[1]))
            
        