class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=list(set(nums1))
        b=list(set(nums2))
        for i in a.copy():
            for j in b.copy():
                if i==j:
                    a.remove(i)
                    b.remove(j)
        lst=[a]+[b]
        return lst