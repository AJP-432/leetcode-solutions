from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution: O(n), O(n)
        # The max count of a given item is the size of nums
        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets)
        
        # Need to not use the k variable again (such an annoying bug ...)
        for key, count in Counter(nums).items():
            buckets[count].append(key)
        
        res = [] 
        # Go through the buckets from most to least frequent
        for i in range(len(buckets) - 1, -1, -1):
            # A bucket may have >1 num
            for num in buckets[i]:
                res.append(num)

                if len(res) == k: 
                    return res
        
        return [] 