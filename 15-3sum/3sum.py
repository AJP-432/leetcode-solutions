class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution: O(n^2), O(1)
        res = []

        nums.sort()
        for i in range(len(nums)):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                print(f"Skipping: {nums[i]} and {nums[i-1]}")
                continue

            target = -1 * nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r: 
                m = nums[l] + nums[r]
                if m < target: 
                    l += 1
                
                elif m > target: 
                    r -= 1
                
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    # Move one (either works)
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1                    
        
        return res
