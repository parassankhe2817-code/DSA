class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even=0
        for i in nums:
            a=len(str(i))
            if a%2==0:
                even+=1
        return even
        