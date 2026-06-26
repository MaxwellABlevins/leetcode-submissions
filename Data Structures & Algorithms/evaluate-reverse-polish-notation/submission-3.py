class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens) == 0:
            return 0

        operand = []

        for i, v in enumerate(tokens):
            if v.isdigit() or (len(v) > 1 and v[0] == '-'):
                operand.append(int(v))
            elif v == "+":
                operand.append(operand.pop() + operand.pop())
            elif v == "-":
                second = operand.pop()
                first = operand.pop()
                operand.append(first - second)
            elif v == "*":
                operand.append(operand.pop() * operand.pop())
            elif v == "/":
                second = operand.pop()
                first = operand.pop()
                operand.append(int(first / second))

        return operand[0]