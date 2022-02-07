class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        solution = []
        
        
        def next_move(openb,closedb,state):
            
            if(openb<n and closedb<openb):
                return [state+"(",state+")"]
            
            elif(openb<n):
                return [state+"("]
                
            elif(closedb<n and openb==n):
                return [state+")"]
        
        
        def all_possiblities(openb,closedb,state):
            if openb==closedb==n:
                solution.append(state)
                
            else:
                next_possiblity = next_move(openb,closedb,state)
            
                for i in next_possiblity:
                    if i[-1]=="(":
                        all_possiblities(openb+1,closedb,i)
                    
                    elif i[-1]==")":
                        all_possiblities(openb,closedb+1,i)
                        
                        
        all_possiblities(0,0,"")
        
        return solution
                
            
            
            
                
            
                    
                
            
        
        
#         if(n==1):
#             return["()"]
        
#         elif(n==2):
#             return ["(())","()()"]
        
#         else:
#             a = self.generateParenthesis(n-1)
#             hashmap={}
            
#             for i,e in enumerate(a):
#                 hashmap["()"+e]=1
#                 hashmap["("+e+")"]=1
#                 hashmap[e+"()"]=1
                
#             return hashmap.keys()

      
                
        
        