class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        stack = [-1]
        newtop = 0 
        cur_max = 0 
        
        if(s==""):
            return 0
         
        for i in range(len(s)):
            
            if(s[i]=="("):
                stack.append(i)
                
            if(s[i]==")"):
                if(stack[-1]!=(-1) and s[stack[-1]]=="("):
                    stack.append(i)
                    temp_max = i-stack[-3]
                    if(temp_max>cur_max):
                        cur_max = temp_max 
                    
                    stack.pop()
                    stack.pop() 
                
                else:
                    stack.append(i)
        
        return cur_max 
                    
                           
                        
                    
                