class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result=[]

        common=set(nums1) & set(nums2) #{9,4}

        for i in common:
            count1=nums1.count(i)
            count2=nums2.count(i)

            for j in range(min(count1,count2)):
                result.append(i)
        return result
                