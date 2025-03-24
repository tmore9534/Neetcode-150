# https://leetcode.com/problems/valid-anagram/description/
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False
        # avoid hashMap and use list (only works if characters are English letters not unicode)
        hash_s = [0] * 26
        hash_t = [0] * 26
    
        for i in range(len(s)):
            hash_s[ord(s[i]) - ord("a")] += 1
            hash_t[ord(t[i]) - ord("a")] += 1
            
        return all(hash_s[i] == hash_t[i] for i in range(len(hash_s)))





    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
        
    #     return collections.Counter(s) == collections.Counter(t)