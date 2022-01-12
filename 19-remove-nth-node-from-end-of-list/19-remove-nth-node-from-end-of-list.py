# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        
        l = 0
        lst = []
        
        copy = head
        
        while copy !=None:
            lst.append(copy.val)
            l=l+1
            copy = copy.next
            
        lst.reverse()
        
        pos = l-n 
        
        copy = None
        
        def insert(copy,v):
            if(copy==None):
                return ListNode(v,None)
                
            return ListNode(v,copy)
        
        
        for i in range(l):
            if(i!=(n-1)):
                copy=insert(copy,lst[i])
                
        return copy