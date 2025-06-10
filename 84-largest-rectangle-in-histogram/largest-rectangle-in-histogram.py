class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Solution: O(n), O(n)

        # Keep a monotic stack of increasing heights; 
        # if left over after main loop, process  

        best = 0
        # format: (height, idx)
        stack = [] 
        for i, h in enumerate(heights): 
            # Consider the area of just this rectangle (width = 1)
            best = max(best, h)

            if not stack or stack[-1][0] <= h: 
                stack.append((h, i))
            
            else: 
                furthest = None
                # This rectangle can not be grown more, compute it
                while stack and stack[-1][0] > h: 
                    o_h, o_idx = stack.pop()
                    # -1 as we can not consider the width of the current bar
                    area = o_h * (i - o_idx)
                    best = max(best, area)

                    # We know the rectangle at o_idx has o_h > h, 
                    # that means that the current rectangle can in 
                    # fact start from there!
                    furthest = o_idx
                
                stack.append((h, furthest))

        # These bars can extend to the end of the graph
        while stack: 
            h, i = stack.pop()
            area = h * (len(heights) - i)
            best = max(best, area)
        
        return best

        


