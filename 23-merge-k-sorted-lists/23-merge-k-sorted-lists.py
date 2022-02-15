# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq 

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if (lists==[]):
            return None
                
            
        bool = True 
        
        dict = {}
        
        result = None 
        
        for i in range(len(lists)):
            if(lists[i] is not None):
                bool = False 
                dict[i] = (lists[i].val)
                lists[i] = lists[i].next
                
                
                
        if(bool):
            return None 
        

        heap = dict.values()
        heapify(heap)
        
        while(heap!=[]):
            
            max_el = heappop(heap)
            
            result = ListNode(max_el,result)
            
            
            for i in dict.keys():
                if(dict[i]==max_el):
                    if(lists[i] is not None):
                        heappush(heap,lists[i].val)
                        dict[i] = lists[i].val
                        lists[i] = lists[i].next
                
                
        final = None
        
        while (result is not None):
            final = ListNode(result.val,final)
            result = result.next
            
        return final
            
            
            
        
        
#         for i in range(len(lists)):
#             if(lists[i] is None): 
#                 pass
                
            
#             else:
#                 if(lists[i].val<min_val):
#                     min_val = lists[i].val
#                     pointer = i 
                    
#                 else:
#                     pass 
                
#         lists[pointer] = lists[pointer].next
        

#         return (ListNode(min_val,self.mergeKLists(lists)))
            
            
        