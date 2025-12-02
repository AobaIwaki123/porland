def porland(S: str):
    stack = []
    ans = 0
    for c in S:
        if c in "+-*/":
            match c:
                case "+":
                    ans = stack[-2] + stack[-1]
                case "-":
                    ans = stack[-2] - stack[-1]
                case "/":
                    ans = stack[-2] / stack[-1]
                case "*":
                    ans = stack[-2] * stack[-1]
            stack.pop(-1)
            stack.pop(-1)
            stack.append(ans)
        else:
            stack.append(int(c))
    return ans
