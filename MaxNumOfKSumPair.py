class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        i, j = 0, len(nums)-1
        while i < j:
            sums = nums[i] + nums[j]
            if sums == k:
                ans += 1
                i, j = i+1, j-1
            elif sums > k:
                j = j-1
            else:
                i = i+1
        return ans
