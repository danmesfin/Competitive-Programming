class MinStack:

    def __init__(self):
        self.stack = []
        self.stackmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stackmin or val <= self.stackmin[-1]:
            self.stackmin.append(val)
        
    def pop(self) -> None:
        if self.stack[-1] == self.stackmin[-1]:
            self.stackmin.pop()
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmin[-1]
