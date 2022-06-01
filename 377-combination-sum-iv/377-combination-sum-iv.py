class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        arr = [0 for i in range(target+1)]
        
        arr[0]=1
        
        for i in range(1,len(arr)):
            count = 0 
            for j in nums:
                new_target=i-j 
                if(new_target<0):
                    continue
                else:
                    count+=arr[new_target]
                    
            arr[i]=count
            
       
        return arr[-1]
                    
                
                
        
        
        # [1,2,3] 
        
        # [1,2,3]->3 => 4 
        # [1,2,3]->2 => 2 
        # [1,2,3]->1 => 1  
        # (3),(1,2),(2,1),(1,1,1,1)
        # 7 
        # [1,2,3]=> 0
        
        # [1,2,3]-> 3
        # [1,2,3]-> 2
        # [1,2,3]-> 1
        # [1,1,2,4,7]        
        # If I already knew this my algo would be faster 
        
#         if(target<0):
#             return 0
        
#         elif(target==0):
#             return 1 
        
#         count=0 
#         for i in range(len(nums)):
#             new_target = target-nums[i]
#             count += self.combinationSum4(nums,new_target)
            
#         return count  
         
            