class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution: O(n), O(n)
        p = s = 1
        prefix = [1] + [p := p * n for n in nums]
        suffix = [s := s * n for n in nums[::-1]][::-1] + [1]

        res = [] 
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i + 1])

        return res