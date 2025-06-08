class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Key insight: a start of a "thread" needs to be 
        # a num for which num - 1 not in nums

        # Solution: O(n), O(n)
        longest = 0
        data = set(nums)
        # Iterate the set to avoid duplicate thread exploration
        for n in data: 
            # Start of a thread
            if n - 1 not in data: 
                count = 1
                while n + count in data:
                    count += 1
            
                longest = max(longest, count)
        
        return longest