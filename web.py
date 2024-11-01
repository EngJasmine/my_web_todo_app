import streamlit as st
import functions

todos=functions.get_todos()
#Method allowing to config the page
st.set_page_config(layout='wide')
def add_todo():
    to_do=st.session_state['new_todo']+ '\n'
    todos.append(to_do )
    functions.write_todos(todos)
    st.session_state['new_todo']=''

st.title("My TODO Application")
st.subheader('This is my todo App.')
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

for index,todo in enumerate(todos):
    check_box=st.checkbox(todo,key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label=' ',placeholder='Add new todo',
              on_change=add_todo,key='new_todo')