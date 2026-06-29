class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = list(set(nums))
        return len(unique_nums) != len(nums)
        