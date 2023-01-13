class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set([i for i in nums])) != len(nums)
