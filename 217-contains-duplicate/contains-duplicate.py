class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution: O(logn), O(1)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False

        # Another solution: O(n), O(n)
        # seen = set()
        # for n in nums: 
        #     if n in seen: 
        #         return True
            
        #     seen.add(n)
        
        # return False
        
        # Another solution: O(n), O(n)
        # return len(nums) != len(set(nums))