from math import floor, ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_map = {
            "+": lambda a, b: a + b, 
            "-": lambda a, b: a - b, 
            "*": lambda a, b: a * b, 
            "/": lambda a, b: floor(a / b) if a / b > 0 else ceil (a / b)
        }
        
        stack = []
        for t in tokens: 
            if t not in op_map:
                stack.append(int(t))
            
            else: 
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(op_map[t](n1, n2))
        
        return stack.pop()