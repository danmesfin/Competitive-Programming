class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        indx = n - k
        res = nums[indx:] + nums[:indx]
        for i in range(n):
            nums[i] = res[i]
        return
