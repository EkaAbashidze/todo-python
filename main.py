todos = []

while True:
    user_action = input("Type add, show, edit or exit: ").strip().lower()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            editing = input(f'Enter a new text for this todo: {todos[number - 1]}')
            todos[number - 1] = editing
            print(todos[number - 1])
        case "show":
            for index, item in enumerate(todos):
                item = item.title()
                print(f'{index + 1}) {item}')
            break
        case "exit":
            break
        case _:
            print("You entered an unknown command")

print("Bye!")