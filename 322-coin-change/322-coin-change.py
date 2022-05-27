class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        
        # how to optimize this 
        
        # DP table 
        # last move 
        
        # 10,9,6 
        # 1 coin and obtain 11 
        
        arr = [0 for i in range(amount+1)]
        arr[0]=0 
                    
        for i in range(1,amount+1):
            min_coin = None
            
            for j in coins:
                amount_to_make = i-j
                if(amount_to_make>=0):
                    if(arr[amount_to_make]!=-1):
                        if(min_coin is None):
                            min_coin = arr[amount_to_make]+1
                        else:
                            min_coin = min(min_coin,arr[amount_to_make]+1)
            
            if(min_coin is None):
                arr[i]=-1
                
            else:
                arr[i]=min_coin
                    
        
        return arr[amount]
            
               
            
         
                    
                    
                
                
                
                
        
        