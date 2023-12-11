def get_todos(file_path="todo.txt"):
    with open(file_path, "r") as file_todo:
        temp_todos = file_todo.readlines()
        return temp_todos


def set_todos(temp_todos, file_path="todo.txt"):
    with open(file_path, "w") as file_todo:
        file_todo.writelines(temp_todos)
        return True

