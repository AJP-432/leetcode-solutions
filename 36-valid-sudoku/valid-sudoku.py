class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Solution: O(n), O(n)
        # Need to check uniqueness of rows, cols, and sub-squares

        # Row and col check 
        for r in range(9):
            row_items = set()
            col_items = set()
            for c in range(9):
                n = board[r][c]
                m = board[c][r]
                if (n != "." and n in row_items) or (m != "." and m in col_items): 
                    return False
                
                row_items.add(n)
                col_items.add(m)

        # Subsquare check (go through all 3x3s)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for r in range(i, i + 3): 
                    for c in range(j, j + 3): 
                        n = board[r][c]
                        if n != "." and n in seen: 
                            return False
                    
                        seen.add(n)
        
        return True
                
