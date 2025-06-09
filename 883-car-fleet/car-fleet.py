from math import ceil 

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort by position
        ps = sorted(zip(position, speed), key=lambda x: x[0])
        # Time to reach
        ttr = [(target - p) / s for p, s in ps]
        print(ttr)

        stack = [] 
        for time in ttr: 
            # If we are going to slow down a previous car 
            # such that it joins our fleet
            while stack and stack[-1] <= time: 
                stack.pop()
            
            stack.append(time)


        return len(stack)