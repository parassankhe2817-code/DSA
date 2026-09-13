class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        b=[]
        for i in nums:
            a=len(str(i))
            if a%2==0:
                b.append(a)
        return len(b)
        