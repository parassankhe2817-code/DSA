class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[i]==nums[j]:
                nums[i]="k"
            i+=1
        while "k" in nums:
            nums.remove("k")
        
        return len(nums)
        return nums
        