class Solution:
    def EQDistance(self, point:List[float]):
        return sqrt(point[0]**2 + point[1]**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # mylist = self.EQDistance(points[1])
        points.sort(key = self.EQDistance)
        closest = []
        for i in range(0,k,1):
            closest.append(points[i])
        return closest
