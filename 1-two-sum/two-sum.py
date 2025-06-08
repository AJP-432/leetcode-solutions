class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution: O(n), O(n)
        seen = {}
        for i, n in enumerate(nums): 
            needed = target - n
            if needed in seen:
                return [seen[needed], i]
            
            seen[n] = i
        
        return []