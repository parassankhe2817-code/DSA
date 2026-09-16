class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lst=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    lst.append(i)
                    lst.append(j)
        return lst
        