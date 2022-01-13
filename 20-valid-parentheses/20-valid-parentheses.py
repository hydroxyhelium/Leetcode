class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        hashmap={")":"(","}":"{","]":"["}
        
        
        
        def cond(a):
            return (a=="(" or a=="{" or a =="[")
        

        
        if(s[0]=="(" or s[0]=="{" or s[0]=="["):
            for i in range(len(s)):
                if(cond(s[i])):
                    stack.append(s[i])
                else:
                    if(stack==[]):
                        return False
                    
                    if(hashmap[s[i]]==stack[-1]):
                        stack.pop()
                        
                    else:
                        
                        return False 
                    
            if(stack==[]):
                return True 
            
            else:
                return False
        
        else:
            if(s!=""):
                return False
            
            else:
                return True 
        
        
                