import function
import streamlit as st
import time

# todo connected to github!!!hahahahahah

todos = function.get_todos()


def add_todo():
    if st.session_state["new_todo"]:
        todo = st.session_state["new_todo"] + "\n"
        todos.append(todo)
        function.write_todos(todos)


st.title("My Todo App")
st.subheader("Yeah...hello")
st.write("This app is to increase your productivity.")
st.write(f"{time.strftime('%Y年%m月%d日')}")


for i, todo in enumerate(todos):
    todo_text = f"{i+1}-{todo}"
    checkbox = st.checkbox(todo_text, key=todo_text)
    if checkbox:
        todos.pop(i)
        function.write_todos(todos)
        del st.session_state[todo_text]
        st.experimental_rerun()


inputx = st.text_input(label="What's on your mind?",
                       placeholder="Add new todo...",
                       key="new_todo",
                       on_change=add_todo)




