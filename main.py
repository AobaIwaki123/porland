def porland(S: str):
    stack = []
    ans = 0
    for c in S:
        if c in "+-*/":
            print("calc")
            match c:
                case "+":
                    ans = int(stack[-1]) + int(stack[-2])
                case "-":
                    ans = int(stack[-1]) - int(stack[-2])
                case "/":
                    ans = int(stack[-1]) / int(stack[-2])
                case "*":
                    ans = int(stack[-1]) * int(stack[-2])
            stack.pop(-1)
            stack.pop(-1)
        else:
            stack.append(c)
        print(stack)
    if (len(stack) > 0):
        raise ValueError("Stack Has Value", stack)
    print("Answer:", ans)

def main():
    A = "11+"
    porland(A)


if __name__ == "__main__":
    main()
