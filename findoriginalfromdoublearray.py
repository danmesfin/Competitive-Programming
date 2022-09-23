class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
       
        changed.sort()
        i = 0
        j = 0
        ans = []
        
        marked = [0] * len(changed)
        while(i < len(changed) and j < len(changed)):
            
            if marked[i] == 0:
                f = 0
                while(j < len(changed)):
                    if changed[j] == changed[i] * 2 and i!=j:
                        marked[i] = 1
                        marked[j] = 1
                        ans.append(changed[i])
                        i += 1
                        j += 1
                        f = 1
                        break
                    else:
                        j += 1
                if f == 0:
                    return []
            else:
                i += 1
        if len(ans) != len(changed) // 2:
            return []
        return ans
