class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        solutions=[]
        reuslt = []
        
        
        def next_move(state):
            
            allowed = [i for i in range(n)]
            
            if(state==[]):
                return [[i] for i in range(n)]
            
            for i in range(len(state)):
                pos = state[i]
                
                if(pos in allowed):
                    allowed.remove(pos)
                
                diagonal1 = pos+(len(state)-i)
                
                if(0<=diagonal1<=n-1):
                    if(diagonal1 in allowed):
                        allowed.remove(diagonal1)
                
                diaganal2 = pos-(len(state)-i)
                
                if(0<=diaganal2<=n-1):
                    if(diaganal2 in allowed):
                        allowed.remove(diaganal2)
                    
            copy = [i for i in state]
            res =[]
            
            for i in allowed:
                copy.append(i)
                res.append([i for i in copy])
                copy.pop()
                
            return res 
            
        def all_possible(state):
            if(len(state)==n):
                solutions.append([i for i in state])
                
            else:
                next_moves = next_move(state)
                
                
                if (next_moves is not None):
                
                    
                    for i in range(len(next_moves)):
                        
                        all_possible(next_moves[i])
                    
        all_possible([])
        
        return(len(solutions))