from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def counter(word) -> Tuple[int]:
            # 26 lowercase english chars
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord("a")] += 1
            
            return tuple(count)

        ana_groups = defaultdict(list)
        for s in strs: 
            # Counter from collections is not hashable
            ana_groups[counter(s)].append(s)
        
        return list(ana_groups.values())