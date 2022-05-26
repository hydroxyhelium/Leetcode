class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #[7,1,5,3,6,4]
        # see profit for each element
        
        # you want the min element on the left and max on the right
        # if you get min, you switch min, but still keep profit 
        
        # greedy algorithm 
        
        max_profit = 0 
#         for i in range(len(prices)):
#             for j in range(i,len(prices)):
#                 profit= prices[j]-prices[i]
                
#                 max_profit = max(profit,max_profit)
                
#         return max_profit 
    
    
        #edge cases later 
        min_ele = prices[0]
        
        for i in range(len(prices)):
            cur_profit= prices[i]-min_ele
            max_profit = max(max_profit,cur_profit)
            min_ele = min(min_ele,prices[i])
            
        return max_profit
            
            
            
              
            
            