history = []
forward_stack = []
visit_count = {}


def visit_page(page):
    history.append(page)
    
    forward_stack.clear()

    visit_count[page] = visit_count.get(page, 0) + 1

    print(f"Visited: {page}")


def go_back():
    if not history:
        print("No pages in history.")
        return

    last_page = history.pop()
    forward_stack.append(last_page)

    print(f"Going back from: {last_page}")

    if history:
        print(f"Current page: {history[-1]}")
    else:
        print("No pages left in history.")


def go_forward():
    if not forward_stack:
        print("No pages to go forward to.")
        return

    next_page = forward_stack.pop()
    history.append(next_page)

    print(f"Going forward to: {next_page}")
    print(f"Current page: {next_page}")


def show_history():
    if not history:
        print("History is empty.")
        return

    print("History: ", end="")
    for i, page in enumerate(history):
        print(f"{page}({visit_count.get(page, 0)})", end="")
        if i != len(history) - 1:
            print(" -> ", end="")
    print()


def count_visits():
    page = input("Enter page name: ")
    count = visit_count.get(page, 0)
    print(f"Page {page} visited {count} times.")


def menu():
    while True:
        print("\n1. Visit Page")
        print("2. Back")
        print("3. Show History")
        print("4. Forward")
        print("5. Count Visits")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            page = input("Enter page name: ")
            visit_page(page)

        elif choice == "2":
            go_back()

        elif choice == "3":
            show_history()

        elif choice == "4":
            go_forward()

        elif choice == "5":
            count_visits()

        elif choice == "6":
            print("Exiting browser simulation.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()
