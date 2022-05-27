"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):   
    
    def cloneGraph(self, node,hashset=None,hashmap=None):
        """
        :type node: Node
        :rtype: Node
        """
        
        if(hashmap is None):
            hashmap={}
            
        if(hashset is None):
            hashset=set()
            
        if(node is None):
            return
        
        # we create temp Node in hashmap
        
        if(node.val in hashset):
            return hashmap[node.val]
        
        else:
            new_node = Node(node.val)
            hashset.add(node.val)
            hashmap[node.val]=new_node
            
            for i in node.neighbors:
                   hashmap[node.val].neighbors.append(self.cloneGraph(i,hashset,hashmap))
                
            return hashmap[node.val]
            
        
                
            
                    
        
    
        
        
        