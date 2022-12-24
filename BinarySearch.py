class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        j= -1
        while((low<=high) and (j== -1)):
            mid = (low+high)//2
            if target == nums[mid]:
                j=mid
            elif (target < nums[mid]): 
                high = mid-1
            else : 
                low = mid+1
        return j
