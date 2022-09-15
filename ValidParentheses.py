class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ['(', '{', '[']:
                stack.append(x)
            else:
                if stack and ((x == ')' and stack[-1] == '(') or (x == '}' and stack[-1] == '{') or (x == ']' and stack[-1] == '[')):
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False
