class Solution(object):
    
    def help(self,nums,val):
        flag = False 
        copy = [x for x in nums]
        for i in range(len(nums)):
            if(flag):
                break
            else:
                if(copy[i]==val):
                    copy = copy[:i]+copy[i+1:]
                    flag = True 
                    
        return copy
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if(len(nums)==1):
            return [[nums[0]]]
        
        elif(nums==[]):
            return []
        
        hashmap = {}
        
        total_combinations = []
        
        for i in range(len(nums)):
            if(nums[i] in hashmap.keys()):
                hashmap[nums[i]] += 1 
                
            else:
                hashmap[nums[i]] = 1
                
            
        for i in hashmap.keys():
            remaning = self.help(nums,i)
            temp = [[i]+x for x in self.permuteUnique(remaning)]
            total_combinations += temp
            
        return total_combinations