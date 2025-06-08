# from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution: O(n), O(n)
        if len(s) != len(t): 
            return False

        # 26 lowercase english chars
        count_s = [0] * 26
        count_t = [0] * 26
        for si, ti in zip(s, t):
            count_s[ord(si) - ord("a")] += 1
            count_t[ord(ti) - ord("a")] += 1
        
        return count_s == count_t

        # Another solution: O(n), O(n)
        # return Counter(s) == Counter(t)