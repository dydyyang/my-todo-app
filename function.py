def get_todos(filepath="todo.txt"):
    """ read a text file and return the list of
    to-do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todo.txt"):
    """Write the to-do items list in the text file."""

    with open(filepath, "w") as file:
        file.writelines(todos_arg)


# def show_todos(filepath="todo.txt"):
#     """Print the to do items in the todo file."""
#     with open (filepath, "r") as file_local:
#         todos_local = file_local.readlines()
#     for i, todo in enumerate(todos_local):
#         print(f"{i+1}-{todo}", end="")


# def edit_todo(filepath="todo.txt"):
#     """Print the to do items, ask the user which one to edit, and the new todo,then edit it."""
#     show_todos(filepath="todo.txt")
#     edit_index = int(input("The above are the todos, which one would you like to edit? Give me the number."))-1
#     new_todo_content = input("what's the new todo on your mind?")
#     with open(filepath, "r") as file_local:
#         todos_local = file_local.readlines()
#     todos_local[edit_index] = new_todo_content
#
#     with open(filepath, "w") as file:
#         file.writelines(todos_local)
#
#
# def complete_todo(filepath="todo.txt", user_action1=""):
#     """delete the completed todo item """
#     if user_action1[-1].isdigit():
#         complete_index = int(user_action1[9:])-1
#     else:
#         show_todos(filepath="todo.txt")
#         complete_index = int(input("The above are the todos, which one would you like to edit? Give me the number."))-1
#
#     with open(filepath, "w") as file:
#         file.writelines(get_todos().pop(complete_index))












