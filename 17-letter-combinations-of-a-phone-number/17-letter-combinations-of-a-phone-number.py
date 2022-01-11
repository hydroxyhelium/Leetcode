class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        output = []
        
        temp_out = []
        
        for i in range(len(digits)):
            temp_out = [j for j in output]
            output = []
            
            if(digits[i]=="2"):
                c = ["a","b","c"]
                
                if(temp_out==[]):
                    output = c
                    
                    
                else:
                    for i in range(len(temp_out)):
                        for j in range(len(c)):
                            output.append(temp_out[i]+c[j])
            
        
            elif(digits[i]=="3"):
                
                c = ["d","e","f"]
                
                if(temp_out==[]):
                    output = c
                    
                    
                else:
                    for i in range(len(temp_out)):
                        for j in range(len(c)):
                            output.append(temp_out[i]+c[j])
                
            
            elif(digits[i]=="4"):
                
                c = ["g","h","i"]
                
                if(temp_out==[]):
                    output = c
                    
                    
                else:
                    for i in range(len(temp_out)):
                        for j in range(len(c)):
                            output.append(temp_out[i]+c[j])
                
            
            
            elif(digits[i]=="5"):
                
                c = ["j","k","l"]
                
                if(temp_out==[]):
                    output = c
                    
                    
                else:
                    for i in range(len(temp_out)):
                        for j in range(len(c)):
                            output.append(temp_out[i]+c[j])
                
            elif(digits[i]=="6"):
                
                c = ["m","n","o"]
                
                if(temp_out==[]):
                    output = c
                    
                    
                else:
                    for i in range(len(temp_out)):
                        for j in range(len(c)):
                            output.append(temp_out[i]+c[j])
                
                
            elif(digits[i]=="7"):
                
                c = ["p","q","r","s"]
                
                if(temp_out==[]):
                    output = c
                    
                    
                else:
                    for i in range(len(temp_out)):
                        for j in range(len(c)):
                            output.append(temp_out[i]+c[j])
                
                
            elif(digits[i]=="8"):
                c = ["t","u","v"]
                
                if(temp_out==[]):
                    output = c
                    
                    
                else:
                    for i in range(len(temp_out)):
                        for j in range(len(c)):
                            output.append(temp_out[i]+c[j])
                
                
            elif(digits[i]=="9"):  
                c = ["w","x","y","z"]
                
                if(temp_out==[]):
                    output = c
                    
                    
                else:
                    for i in range(len(temp_out)):
                        for j in range(len(c)):
                            output.append(temp_out[i]+c[j])
                            
        return (output)
                
        