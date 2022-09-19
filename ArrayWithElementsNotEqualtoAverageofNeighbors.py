class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        size = len(nums)
        m = median(nums)
        
        newArr = [0]*size
        ev=0
        od = 1
        
        for i in range(0,size):
            if nums[i] < m:
                newArr[od] = nums[i]
                od += 2
            else:
                newArr[ev] = nums[i]
                ev += 2
        return newArr
