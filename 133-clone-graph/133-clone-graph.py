"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if(not node):
            return None 
        
        hashmap = {}
        
        # stores [val:node]
        hashmap[node.val]=Node(node.val, None)
        
        tobe = []
        
        for j in node.neighbors:
            copy = Node(j.val,None)
            hashmap[node.val].neighbors.append(copy)
            hashmap[j.val]=copy
            tobe.append(j)
           
        
        #pre-condition, any node has been created
        while(tobe):
            n1 = tobe[0]
            
            for j in n1.neighbors:
                
                if(j.val in hashmap.keys()):
                    hashmap[n1.val].neighbors.append(hashmap[j.val])
                    
                else:
                    copy = Node(j.val,None)
                    hashmap[j.val]=copy
                    tobe.append(j)
                    hashmap[n1.val].neighbors.append(hashmap[j.val])
            
            tobe.pop(0)
        
        return hashmap[node.val]
                    
            
            
            
        

        
        
                    
                