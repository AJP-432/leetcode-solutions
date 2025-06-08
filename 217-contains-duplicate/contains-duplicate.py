class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums: 
            if n in seen: 
                return True
            
            seen.add(n)
        
        return False
        
        # Another solution: 
        # return len(nums) != len(set(nums))