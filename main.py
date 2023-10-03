todos = []

while True:
    user_action = input("Type add, show, or exit: ").strip().lower()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(f'{index + 1}) {item}')
            break
        case "exit":
            break

print("Bye!")