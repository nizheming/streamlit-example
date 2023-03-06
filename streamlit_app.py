import streamlit as st

# Initialize cells list
if "cells" not in st.session_state:
    st.session_state['cells'] = []
cells = st.session_state.cells

# Define a function to add a new cell
def add_cell(cell_type):
    cells.append({"type": cell_type, "content": "", "has_run": False})

# Define a function to delete a cell
def delete_cell(index):
    del cells[index]

ai_responses = {
    "有哪些表": """
TPC-H是一个基准测试套件，用于评估关系型数据库管理系统(RDBMS)在执行复杂的决策支持查询时的性能。该套件包含多个表，用于模拟数据仓库的典型数据结构。以下是TPC-H中包含的表格以及它们的含义：
    Customer（顾客）：模拟一个客户表，包含有关客户的信息，如姓名、地址、市场细分、收入、订单历史记录等。
    Nation（国家）：模拟一个国家表，包含有关各个国家的信息，如名称、地区、GDP等。
    Region（地区）：模拟一个地区表，包含有关各个地区的信息，如名称、国家等。
    Part（零件）：模拟一个零件表，包含有关各个零件的信息，如名称、供应商、类型等。
    Supplier（供应商）：模拟一个供应商表，包含有关供应商的信息，如名称、地址、联系人、历史记录等。
    PartSupp（零件供应商）：模拟一个零件供应商表，包含有关每个供应商提供的每个零件的信息，如成本、供货数量等。
    Orders（订单）：模拟一个订单表，包含有关订单的信息，如订单号、日期、顾客等。
    LineItem（订单行项目）：模拟一个订单行项目表，包含有关每个订单的详细信息，如零件号、数量、成本等。
这些表在TPC-H基准测试中被广泛使用，以评估关系型数据库管理系统在执行决策支持查询时的性能。""",

}

# Define a function to run a cell
def run_cell(index):
    if cells[index]["type"] == "markdown":
        st.markdown(cells[index]["content"])
    elif cells[index]["type"] == "sql":
        # Execute the SQL code here
        st.write("Executing SQL code...")       
    elif calls[index]["type"] == "ai":
        content = cells[index]["content"]
        for k, v in enumerate(ai_responses):
            if k in content:
                st.write(v)
                break
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
    if st.sidebar.button("Add AI Cell"):
        add_cell("ai")

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
                f"SQL", cell["content"], height=60, key=i, placeholder="SQL", label_visibility="collapsed")
        elif cell["type"] == "ai":
            cell["content"] = col1.text_area(
                f"AI", cell["content"], height=30, key=i, placeholder="Your Question", label_visibility="collapsed")
        if col2.button(f"Run", key=f'{i}.1') or run_all or cell["has_run"]:
            run_cell(i)

        if col2.button(f"Delete", key=f'{i}.2'):
            delete_cell(i)
            st.experimental_rerun()
            break


# Run the app
if __name__ == "__main__":
    app()
