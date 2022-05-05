class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if(target==0):
            return [[]]
        
        elif (candidates==[]):
            return []
        
        else:
            first = candidates[0]
            route1 = []
            
            if(target-first>=0):
                route1 = self.combinationSum(candidates,target-first)
            
            if(route1!=[]):
                for i in range(len(route1)):
                    route1[i]=[first]+route1[i]
                    
            route2 = self.combinationSum(candidates[1:],target)
            
            if(route2==[] and route1==[]):
                return []
            
            elif(route1==[]):
                return route2
            
            else:
                return route1+route2
                    
                
            
                