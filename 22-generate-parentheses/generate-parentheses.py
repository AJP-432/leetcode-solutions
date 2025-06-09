class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] 
        def backtrack(acc, open, close):
            if open == close == n: 
                res.append(acc)
                return
            
            if open < n: 
                backtrack(acc + "(", open + 1, close)
            
            if close < open: 
                backtrack(acc + ")", open, close + 1)
        
        backtrack("", 0, 0)
        return res
            