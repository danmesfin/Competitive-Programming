#brute force solution

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            idx = 0
            temp = 0
            added = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    idx = nums2.index(nums2[j])
                    temp = nums2[j]
                    for k in range(idx, len(nums2)):
                        if nums2[k] > temp:
                            result.append(nums2[k])
                            added = True
                            break
                    if not added:
                        result.append(-1)
        return result


                
