def reverse_string(s):
    stack = []
    for c in s:
        stack.append(c)

    rev = ""
    while stack:
        rev += stack.pop()
    return rev

def is_balanced(expr):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for c in expr:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if not stack:
                print(f"Unmatched closing bracket: {c}")
                return False

            top = stack[-1]
            if pairs[c] != top:
                print(f"Mismatched bracket: {top} and {c}")
                return False

            stack.pop()

    if not stack:
        print("Expression is Balanced and Stack is Empty")
        return True
    else:
        print("Expression is Not Balanced")
        print("Remaining stack elements:", " ".join(stack))
        return False

def undo_operations(input_str):
    stack = []
    for c in input_str:
        if c == '#':
            if stack:
                stack.pop()
        else:
            stack.append(c)

    return "".join(stack)

def main():
    while True:
        print("\n=== Stack Applications Menu ===")
        print("1. Reverse a String")
        print("2. Check Balanced Parentheses")
        print("3. Undo Operations (use # as undo)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            s = input("Enter string: ")
            print("Reversed string:", reverse_string(s))

        elif choice == '2':
            expr = input("Enter expression: ")
            is_balanced(expr)

        elif choice == '3':
            s = input("Enter text (use # for undo): ")
            print("Final text after undo:", undo_operations(s))

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
