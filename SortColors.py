class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            mini = i
            for j in range(i,len(nums)):
                if nums[j] < nums[i]:
                    mini = j
                    nums[i],nums[mini] = nums[mini],nums[i]
