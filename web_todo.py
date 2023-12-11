import streamlit as st
import os
import functions


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos = functions.get_todos()
    todos.append(todo)
    functions.set_todos(todos)


if not os.path.exists('todo.txt'):
    with open('todo.txt', 'w') as file:
        pass
if not os.path.exists('todo_history.txt'):
    with open('todo_history.txt', 'w') as file:
        pass

st.title('ToDo App')
st.subheader('Personal Todo List')
st.write("For Increasing my Productivity!!!")

todos = functions.get_todos()
todos_history = functions.get_todos(file_path="todo_history.txt")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.capitalize(), key=f"t{index}")
    if checkbox:
        todos_history.append(todos[index])
        todos.pop(index)
        functions.set_todos(todos)
        functions.set_todos(todos_history, file_path='todo_history.txt')
        st.rerun()

st.text_input(label='', placeholder='Enter a todo...', on_change=add_todo, key='new_todo')

st.subheader('Todo History')

for index, todo in enumerate(todos_history):
    checkbox = st.checkbox(todo.capitalize(), key=f"h{index}", value=True)
    if not checkbox:
        todos.append(todos_history[index])
        todos_history.pop(index)
        functions.set_todos(todos)
        functions.set_todos(todos_history, file_path='todo_history.txt')
