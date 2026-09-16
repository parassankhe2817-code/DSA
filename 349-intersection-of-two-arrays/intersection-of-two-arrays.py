class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a=list(set(nums1))
        b=list(set(nums2))
        lst=[]
        for i in a:
            for j in b:
                if i==j:
                    lst.append(i)
                    
        return lst
        