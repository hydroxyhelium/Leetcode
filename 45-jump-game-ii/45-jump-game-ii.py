class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        le  = len(nums)
        nums.reverse()
        
        #note that this is supposed to be backwards
        
        array = [0 for i in range(le)]

        for i in range(le):
            if(i==0):
                continue 
            else:
                steps = nums[i]
                mi = None
                j = 1 
                
                while(i-j>=0 and j<=steps):
                    if(mi is None):
                        mi = array[i-j]
                        
                    else:
                        if(array[i-j]<mi):
                            mi = array[i-j]
                            
                    j = j+1
                
                if(mi is None):
                    array[i]= 9999999999999999
                else:
                    array[i] = 1+mi
                
        return array[-1]
                
                
            
                        
                #remeber to increment j
                        
                    
                                  
                                  