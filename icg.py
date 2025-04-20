def prec(c):
    """Return precedence of operators."""
    if c == '^':
        return 3
    elif c in ('*', '/'):
        return 2
    elif c in ('+', '-'):
        return 1
    else:
        return -1

def infix_to_postfix(exp):
    """Convert infix expression to postfix notation."""
    stack = []
    postfix = []
    
    for c in exp:
        if c.isalnum():  # Operand
            postfix.append(c)
        elif c == '(':  # Left Parenthesis
            stack.append('(')
        elif c == ')':  # Right Parenthesis
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # pop '('
        else:  # Operator
            while stack and prec(c) <= prec(stack[-1]):
                postfix.append(stack.pop())
            stack.append(c)

    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

def generate_TAC(postfix):
    """Generate Three-Address Code from the postfix expression."""
    stack = []
    tempVarCount = 1
    
    print("\nThree-Address Code:")
    for c in postfix:
        if c.isalnum():  # Operand
            stack.append(c)
        else:  # Operator
            op2 = stack.pop()
            op1 = stack.pop()
            tempVar = f"T{tempVarCount}"
            tempVarCount += 1
            print(f"{tempVar} = {op1} {c} {op2}")
            stack.append(tempVar)

# Main function
if __name__ == "__main__":
    exp = "A+B*C-D/E"  # Input infix expression
    print(f"Infix Expression: {exp}")

    postfix = infix_to_postfix(exp)
    print(f"Postfix Expression: {postfix}")

    generate_TAC(postfix)
