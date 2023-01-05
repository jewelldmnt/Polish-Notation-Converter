def postfix_to_infix(expression):
    stack = []

    # Iterate through the expression
    for char in expression:

        # push the token in the stack if it is an operand
        if char not in ['+', '-', '*', '/'] and char != " ":
            stack.append(char)

        # pop the last two operands in the stack if the token is an operator
        elif char in ['+', '-', '*', '/'] and char != " ":
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            result = f"({operand_1}{char}{operand_2})"
            stack.append(result)

    # popping the last string in the stack
    result = stack.pop()
    # removing the unnecessary parenthesis
    result = result[1:-1]
    return result


def prefix_to_infix(expression):
    # reverse the expression to convert it to postfix

    # initialize an empty stack
    stack = []

    # scanning the token from right to left
    for idx in reversed(range(len(expression))):
        char = expression[idx]
        # push the token in the stack if it is an operand
        if char not in ['+', '-', '*', '/'] and char != " ":
            stack.append(char)

        # pop the last two operands in the stack if the token is an operator
        elif char in ['+', '-', '*', '/'] and char != " ":
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            result = f"({operand_2}{char}{operand_1})"
            stack.append(result)

    # popping the last string in the stack
    result = stack.pop()
    # removing the unnecessary parenthesis
    result = result[1:-1]
    return result


while True:
    print("-" * 30)
    print("MENU".center(30))
    print("-" * 30)
    print("1. Convert prefix to infix")
    print("2. Convert postfix to infix")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            expression = input("Enter the prefix expression: ")
            result = prefix_to_infix(expression)
            assert expression.count("/") or expression.count("+") or expression.count("-") or expression.count("*")
            print("Infix expression: ", result)
            print("\n")
        except AssertionError:
            print("\nYou have entered an invalid expression!\nPlease try again.\n")
        except:
            print("\nYou have entered an invalid expression!\nPlease try again.\n")

    elif choice == '2':
        try:
            expression = input("Enter the postfix expression: ")
            result = postfix_to_infix(expression)
            assert expression.count("/") or expression.count("+") or expression.count("-") or expression.count("*")
            print("Postfix expression: ", result)
            print("\n")
        except AssertionError:
            print("\nYou have entered an invalid expression!\nPlease try again.\n")
        except:
            print("\nYou have entered an invalid expression!\nPlease try again.\n")

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice!\n")
