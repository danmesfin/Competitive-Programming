class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
       
        for ltr in s:
            temp = [] 
            if ltr==')':
                while stack and stack[-1] != '(':
                    top = stack.pop()
                    temp.append(top)
                if stack:stack.pop()
                if temp:stack.extend(temp)
            else: stack.append(ltr)
        return ''.join(stack)                  
