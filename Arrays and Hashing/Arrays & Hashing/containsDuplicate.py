class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set(nums)
        return len(hashSet) != len(nums)