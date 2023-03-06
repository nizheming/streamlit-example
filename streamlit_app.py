import streamlit as st

# Initialize cells list
if "cells" not in st.session_state:
    st.session_state['cells'] = []
cells = st.session_state.cells

# Define a function to add a new cell
def add_cell(cell_type):
    if cell_type == "markdown":
        cells.append({"type": "markdown", "content": "", "has_run": False})
    elif cell_type == "sql":
        cells.append({"type": "sql", "content": "", "has_run": False})

# Define a function to delete a cell
def delete_cell(index):
    del cells[index]

# Define a function to run a cell
def run_cell(index):
    if cells[index]["type"] == "markdown":
        st.markdown(cells[index]["content"])
        cells[index]["has_run"] = True
    elif cells[index]["type"] == "sql":
        # Execute the SQL code here
        st.write("Executing SQL code...")
        cells[index]["has_run"] = True

# Define the Streamlit app
def app():
    # Set the app title
    st.set_page_config(page_title="Jupyter-like App", page_icon=":pencil:")

    # Define the sidebar options
    if st.sidebar.button("Add Markdown Cell"):
        add_cell("markdown")
    if st.sidebar.button("Add SQL Cell"):
        add_cell("sql")

    run_all = False
    if st.sidebar.button("Run all cells"):
        run_all = True


    # Define the main content
    for i, cell in enumerate(cells):
        container = st.container()
        col1, col2 = container.columns([5, 1])

        if cell["type"] == "markdown":
            cell["content"] = col1.text_area(
                f"Text", cell["content"], height=120, key=i, placeholder="Markdown", label_visibility="collapsed")
        elif cell["type"] == "sql":
            cell["content"] = col1.text_area(
                f"SQL", cell["content"], height=120, key=i, placeholder="SQL", label_visibility="collapsed")

        if col2.button(f"Run", key=f'{i}.1') or run_all or cell["has_run"]:
            run_cell(i)

        if col2.button(f"Delete", key=f'{i}.2'):
            delete_cell(i)
            st.experimental_rerun()
            break


# Run the app
if __name__ == "__main__":
    app()
