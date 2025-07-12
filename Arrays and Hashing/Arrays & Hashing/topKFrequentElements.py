import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Here unique means there will not be more than k of top frequent. (it may be possible that same frequency no are there)
        # when the frequency is same, it only contains required elements (from k) of that frequency.
        # k = 2 so [2, 2, 3, 3, 1, 1] will not be there

        n = len(nums)
        # find the counts 
        numberToCount = collections.Counter(nums)

        # use the buckets of count and map the nos, each will contain unique no only since it is guaranteed
        # bucket are going to be 1 - n no
        
        buckets = [[] for _ in range(n + 1)]
        for no, count in numberToCount.items():
            buckets[count].append(no)
    
        ans = []
        for i in range(n, 0 , -1):
            for item in buckets[i]:
                ans.append(item)
            if len(ans) == k:
                return ans
         

        
    