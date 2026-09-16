class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        a=set(nums)
        lst=list(a)
        lst.sort()
        if nums==lst:
            return False
        else:
            return True
        