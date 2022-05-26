class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indx = 0
        indices = []
        nums.sort()
        for num in nums:
            indx += 1
            if num == target:
                indices.append(indx-1)
        return indices
