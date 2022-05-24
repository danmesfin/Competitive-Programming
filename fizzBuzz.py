class Solution:
    def solve(self, num):
        ans = ""
        if num%3 == 0:
            ans += "Fizz"
        if num%5 == 0:
            ans += "Buzz"
        if num%3 != 0 and num%5 != 0:
            ans += str(num)
            
        return ans
        
    def fizzBuzz(self, n: int) -> List[str]:       
        answer = list()
        for num in range(1,n+1,1):
            answer.append(self.solve(num))
        return answer
    
