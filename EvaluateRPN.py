class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            if(x=='+' or x=='-' or x=='*' or x=='/'):
                if x=='+':
                    stack.append(stack.pop() + stack.pop())
                elif x=='-':
                    x1 = stack.pop()
                    x2 = stack.pop()
                    stack.append(x2 - x1)
                elif x=='*':
                    stack.append(stack.pop() * stack.pop())
                elif x=='/':
                    x1 = stack.pop()
                    x2 = stack.pop()
                    stack.append(int(x2 / x1))
            else: stack.append(int(x))
                
        return stack.pop()
                    
