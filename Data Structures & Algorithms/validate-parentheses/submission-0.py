class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        for v in s:
            if len(stack):
                if stack[-1] == "(" and v == ")":
                    stack.pop()
                    continue
                if stack[-1] == "[" and v == "]":
                    stack.pop()
                    continue
                if stack[-1] == "{" and v == "}":
                    stack.pop()
                    continue
            stack.append(v)
        return len(stack) == 0
