class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        flag = n-1 
        index = 0 
        
        for i in range(n):
            j = n-1-i
            
            
            if(j-1>=0 and nums[j-1]>=nums[j]):
                flag = flag-1 
                
            else:
                if(j==0):
                    nums.reverse()
                    return
                
                index=j
                break
            
        switch = 0 
        
        for i in range(index,n):
            if( (i+1)<n and nums[i]>nums[index-1] and nums[i+1]<=nums[index-1]):
                switch = i 
                break 
                
            elif( (i==n-1) and nums[i]>nums[index-1]):
                switch = i
                break
        
        
        nums[index-1],nums[switch]= nums[switch],nums[index-1]
        
        counter = index
        relen = (n-1)-(index)
        
        
        
        if(relen%2==0):
            while(counter-index<(relen)/2):
                nums[counter],nums[n-1-(counter-index)] = nums[n-1-(counter-index)],nums[counter]
                counter = counter+1
                
        else:
            while(counter-index<=(relen)/2):
                nums[counter],nums[n-1-(counter-index)] = nums[n-1-(counter-index)],nums[counter]
                counter = counter+1 
                
            
            
        