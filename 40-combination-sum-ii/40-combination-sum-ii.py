class Solution(object):
    
    
    # assumes that input is given sorted
    def helpercombinationSum2(self,candidates,target):
        
        
        if(target==0):
            return [[]]
        
        elif( target<0 or candidates==[]):
            return []
        
        cur = candidates[0]
        
        
        breakpoint = 0 
        
        
        for i in range(len(candidates)):
            if(candidates[i]==cur):
                pass
            else:
                breakpoint=i
                break
        
       
            
        #print(candidates,candidates[1:], candidates[breakpoint:])
            
        #include but just once 
        option1 = self.helpercombinationSum2(candidates[1:],target-cur)
        
        #don't include 
        if(candidates[0]==candidates[breakpoint]):
            option2 = self.helpercombinationSum2([],target)
            
        else:
            option2 = self.helpercombinationSum2(candidates[breakpoint:],target)
        
        if(option1 == option2 == []):
            return []
        
        elif(option1==[]):
            return option2 
        
        elif(option2==[]):
            return [[cur]+x for x in option1] 
        
        else:
            return [[cur]+x for x in option1]+option2 
        
    
    
    
    
    
    
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        #assume that we are getting the sorted array as our input 
        
        
        candidates.sort()
        
        return self.helpercombinationSum2(candidates,target)