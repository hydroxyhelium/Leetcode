# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def reverseKGroup(self, head, k,res=None):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        arr = []
        copy = head 
        enough = True
        
        def reverse(head):
            copy = None
            
            while(head):
                copy = ListNode(head.val, copy)
                head = head.next
                
            return copy 
        
        for i in range(k):
            if(head):
                arr.append(head.val)
                head = head.next
                
            else:
                enough= False
                break 
         
        if(not enough):
            
            while(copy):   
                res = ListNode(copy.val,res)
                copy = copy.next
                
            return reverse(res)           
            
        arr.reverse()
        for i in arr:
            res = ListNode(i,res)   
        
        
            
        return self.reverseKGroup(head,k,res)