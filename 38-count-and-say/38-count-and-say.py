class Solution(object):
    
    
    #returns the next say
    def nextsay(self,string):
        num = []
        count = []
        # each number correponds to the count 
        
        cur = None
        
        
        for i in range(len(string)):
            if(cur is None):
                cur = string[i]
                num.append(cur)
                count.append(1)
                
            else:
                if string[i] == cur:
                    count[-1] = count[-1]+1
                    
                else:
                    cur = string[i]
                    num.append(cur)
                    count.append(1)
        
        news = ""
        
        for i in range(len(num)):
            news = (news+(str(count[i])))+(str(num[i]))
        
       
    
        return news
            
        
    
    
    
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        cur = "1"
        
        if(n==1):
            return "1"
        
        for i in range(n-2):
            cur = self.nextsay(cur)
            
        return self.nextsay(cur)
            