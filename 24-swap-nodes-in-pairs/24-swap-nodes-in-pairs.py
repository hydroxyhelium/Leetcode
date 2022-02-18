# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        res = None
        
        while(head):
            if(head.next is None):
                res = ListNode(head.val,res)
                head = head.next
                
            else:
                cur = (head.val)
                nextv = (head.next).val 
                res = ListNode(cur,ListNode(nextv,res))
                head = (head.next).next
                
                
        copy = None
        
        while(res):
            copy = ListNode(res.val,copy)
            res = res.next
        
        return copy
                
                
                
            