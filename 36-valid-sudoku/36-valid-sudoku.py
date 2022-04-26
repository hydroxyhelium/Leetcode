class Solution(object):
    
   
    
    def isValidSudoku(self, board):
        
        def help_sub(mini):
            cur = []
            
            
            for i in range(3):
                for j in range(3):
                    if(mini[i][j]!="." and mini[i][j] in cur):
                        return False
                    else:
                        cur.append(mini[i][j]) 
                    
            return True 
    
        
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # print([x[0:3] for x in board[0:3]])
        # row validation
        
        for i in range(9):
            row = board[i]
            cur = []
            for j in range(9):
                if (row[j] in cur and row[j]!="."):
                    return False
                cur.append(row[j])        
                
        # column validation
        for i in range(9):
            cur = []
            for j in range(9):
                if (board[j][i] in cur and board[j][i]!="."):
                    return False
                cur.append(board[j][i])        
        
        # submatrix validaiton
        
        
        # print([ x[6:9] for x in board[0:3] ])
        for j in [0,3,6]:
            for z in [0,3,6]:
                
                temp = [ x[z:(z+3)] for x in board[j:(j+3)] ]
            
                if(not (help_sub(temp) )):
                    return False
                
        return True 
                
        
        