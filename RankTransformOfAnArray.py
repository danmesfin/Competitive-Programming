class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ind = [x+1 for x in range(len(arr))]
        tempranks = dict(zip(sorted(set(arr)), ind))
        rank = []
        for i in arr:
            rank.append(tempranks[i])
        return rank
