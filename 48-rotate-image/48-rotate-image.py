class Solution(object):
    
    
    def retobject(self,matrix):
        
        self.rotate(matrix)
        
        return matrix
    
    
    
    
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        if(matrix==[]):
            return 
        
        l = len(matrix)
        
        if(len(matrix)==1):
            return matrix
        
        else:
            row1 = [x for x in matrix[0]]
            row2 = [matrix[i][l-1] for i in range(l)]
            row3 = [x for x in matrix[l-1]]
            row4 = [matrix[i][0] for i in range(l)]
            
            for i in range(l):
                matrix[0][i] = row4[l-1-i]
                matrix[i][l-1] = row1[i]
                matrix[l-1][i] = row2[l-1-i]
                matrix[i][0] = row3[i]
                
            mod= [x[1:-1] for x in matrix[1:-1]]
            
            ret = self.retobject(mod)
            
            for i in range(1,l-1):
                for j in range(1,l-1):
                    matrix[i][j]= ret[i-1][j-1]
                    
            
            