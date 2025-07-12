from typing import List
import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = collections.defaultdict(int)
        
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]
            hashMap[nums[i]] = i