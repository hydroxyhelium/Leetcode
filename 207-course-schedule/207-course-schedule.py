class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        
        # numcourses = 3 
        
        # [[0,1],[1,2],[2,0]] -> A cycle hence GG 
        
        # hashmap[0]=[1]
        # hashmap[1]=[2]
        # hashmap[2]=[0]
        
        
        # [0,1,2]
        
        # hashset()
        
        def check(hashmap,num,hashset):
            # num is an arr
            Bool = False 
            
            for i in num:
                
                if(i not in hashmap.keys()):
                    continue
                    
                if(i in hashset):
                    return False
                
                hashset.add(i)
                new = hashmap[i]
                
                temp_hash = hashset
                
                if( not check(hashmap,new,temp_hash)):
                    return False 
                
                hashmap[i]=[]
                
                hashset.remove(i)
                
                
                
                
                
            return True 
                    
        
        
        arr = [0 for i in range(numCourses)]
        hashmap = {}
        
        for j in range(len(prerequisites)):
            ele = prerequisites[j]
            if(ele[0] in hashmap.keys()):
                hashmap[ele[0]].append(ele[1])
                
            else:
                hashmap[ele[0]]=[ele[1]]
                
        Bool = False
        
        for k in range(numCourses):
            if(k in hashmap.keys()):
                hashset = set()
                hashset.add(k)
                if(not check(hashmap,hashmap[k],hashset)):
                    print(k)
                    return False
                
            else:
                continue
                
        return True
                
            
        
            