class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        for i in candies:
            sum=i+extraCandies
            if sum>=max(candies):
                a.append(True)
            else:
                a.append(False)
        return a
        