def porland(S: str):
    stack = []
    ans = 0
    for c in S:
        if c in "+-*/":
            match c:
                case "+":
                    ans = int(stack[-2]) + int(stack[-1])
                case "-":
                    ans = int(stack[-2]) - int(stack[-1])
                case "/":
                    ans = int(stack[-2]) / int(stack[-1])
                case "*":
                    ans = int(stack[-2]) * int(stack[-1])
            stack.pop(-1)
            stack.pop(-1)
            stack.append(ans)
        else:
            stack.append(c)
    return ans

def main():
    A = "11+"
    porland(A)


if __name__ == "__main__":
    main()
