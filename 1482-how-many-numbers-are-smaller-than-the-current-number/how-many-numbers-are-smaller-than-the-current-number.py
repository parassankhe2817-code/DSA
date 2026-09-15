class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(len(nums)):
            a=0
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:
                    a+=1
            lst.append(a)
        return lst
        