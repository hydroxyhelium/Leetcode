class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        acc1 = 0 
        acc2 = 0 
        
        for i in range(len(num1)):
            acc1 = 10*acc1+int(num1[i])
        
        for j in range(len(num2)):
            acc2 = 10*acc2+int(num2[j])
            
        return str(acc1*acc2)
            
        