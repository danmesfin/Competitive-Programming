class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numString = []
        result = ''
        for i in range(len(nums)):
            numString.append(str(nums[i]))
        for i in range(len(numString)):
            max_idx = i
            for j in range(i+1, len(numString)):
                if numString[j] + numString[max_idx] >= numString[max_idx] + numString[j]:
                    max_idx = j
       
            numString[i],numString[max_idx] = numString[max_idx],numString[i]
           
        for i in range(len(numString)):
            result = result + numString[i]
        if int(result) == 0: 
            return "0" 
        return result
