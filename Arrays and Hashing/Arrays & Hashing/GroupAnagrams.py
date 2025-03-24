from type import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = collections.defaultdict(list)

        for s in strs:
            #convert s in hash
            s_hash = [0] * 26
            for ch in s:
                s_hash[ord(ch) - ord("a")] += 1
        
            groups[tuple(s_hash)].append(s)
        
        return list(groups.values())


    # Time complexity: O(n.26)
    # Space complexity: O(n)