import streamlit as st

def init():
    cells = st.session_state.cells
    cells.append({"type": "ai", "content": "TPCH 有哪些表，分别是什么含义？", "has_run": False})
    cells.append({"type": "ai", "content": "基于这个数据集，我想提升我的利润，有什么方法？", "has_run": False})
    cells.append({"type": "ai", "content": "举几个方式来优化采购成本，并且通过数据展现", "has_run": False})

    # cells.append({"type": "ai", "content": "", "has_run": False})
    # cells.append({"type": "ai", "content": "", "has_run": False})


# Initialize cells list
if "cells" not in st.session_state:
    st.session_state['cells'] = []
    init()
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

    * Customer（顾客）：模拟一个客户表，包含有关客户的信息，如姓名、地址、市场细分、收入、订单历史记录等。
    * Nation（国家）：模拟一个国家表，包含有关各个国家的信息，如名称、地区、GDP等。
    * Region（地区）：模拟一个地区表，包含有关各个地区的信息，如名称、国家等。
    * Part（零件）：模拟一个零件表，包含有关各个零件的信息，如名称、供应商、类型等。
    * Supplier（供应商）：模拟一个供应商表，包含有关供应商的信息，如名称、地址、联系人、历史记录等。
    * PartSupp（零件供应商）：模拟一个零件供应商表，包含有关每个供应商提供的每个零件的信息，如成本、供货数量等。
    * Orders（订单）：模拟一个订单表，包含有关订单的信息，如订单号、日期、顾客等。
    * LineItem（订单行项目）：模拟一个订单行项目表，包含有关每个订单的详细信息，如零件号、数量、成本等。
这些表在TPC-H基准测试中被广泛使用，以评估关系型数据库管理系统在执行决策支持查询时的性能。""",
    "提升我的利润": """
    基于TPC-H数据集，提升利润的方法可能因公司的具体情况而异，但以下是一些可能有帮助的建议：  
    
    * 提高销售额：这是最直接提高利润的方法。您可以分析TPC-H数据集中的订单数据，了解您的客户购买的产品、频率、数量等信息，制定促销计划、优化营销策略，从而提高销售额。
    * 优化采购成本：TPC-H数据集中包含了关于供应商和零件的信息，您可以分析这些数据，寻找潜在的成本节省机会，例如寻找价格更低、质量更好的供应商，优化采购流程等。
    * 控制库存成本：库存成本可能对利润产生重大影响。您可以通过分析TPC-H数据集中的库存信息，了解哪些产品库存较高或滞销，优化库存管理，降低库存成本。
    * 提高生产效率：如果您的公司是制造型企业，提高生产效率也是提高利润的有效方法。您可以通过分析TPC-H数据集中的生产数据，了解生产线瓶颈、生产效率等信息，从而制定优化计划。
    * 了解竞争对手：了解竞争对手的定价策略、产品组合、市场份额等信息，可以帮助您制定更有效的营销策略，提高市场份额和利润。
需要注意的是，以上仅是一些可能有帮助的建议，具体的提升利润方法需要根据您公司的具体情况进行分析和制定。""",
    "优化采购成本": """
    以下是几种可能有帮助的优化采购成本的方式，并且展示如何通过数据来支持这些决策：

    * 寻找价格更低的供应商：您可以通过分析TPC-H数据集中的PartSupp表来了解不同供应商提供的零件价格，进而寻找价格更低的供应商。下面是一种展示零件价格和供应商的方法：
    ``` sql
        SELECT ps.ps_partkey, ps.ps_suppkey, ps.ps_supplycost, s.s_name
        FROM partsupp ps, supplier s
        WHERE ps.ps_suppkey = s.s_suppkey
    ```
        这个查询将返回每个零件的供应商、价格和名称信息。通过分析这些数据，您可以找到提供价格更低的零件供应商。

    * 优化采购流程：优化采购流程可以降低采购成本并提高效率。您可以通过分析TPC-H数据集中的订单和供应商数据，了解订单处理时间、交货时间、发货时间等信息，找到可能存在的瓶颈和优化机会。下面是一个查询，它将返回每个订单的发货时间和交货时间：
    ``` sql
        SELECT o.o_orderkey, o.o_orderdate, o.o_shippriority, l.l_commitdate, l.l_receiptdate
        FROM orders o, lineitem l
        WHERE o.o_orderkey = l.l_orderkey
    ```
        通过分析这些数据，您可以了解订单处理的效率和时间，并找到可以优化的地方，例如缩短订单处理时间、改进交货时间等。

    * 分析供应商绩效：分析供应商绩效可以帮助您了解哪些供应商提供了高质量的产品和服务，从而为您的采购决策提供更好的数据支持。以下是一个查询，它将返回每个供应商的总采购金额、平均采购金额和采购数量：
    ``` sql
        SELECT ps.ps_suppkey, SUM(l.l_extendedprice*(1-l.l_discount)) AS revenue, AVG(l.l_extendedprice*(1-l.l_discount)) AS avg_price, SUM(l.l_quantity) AS quantity
        FROM partsupp ps, lineitem l
        WHERE ps.ps_partkey = l.l_partkey AND ps.ps_suppkey = l.l_suppkey
        GROUP BY ps.ps_suppkey
    ```
        通过分析这些数据，您可以找到提供高质量产品和服务的供应商，并调整您的采购策略，以便更多地从这些供应商采购。
    """
}

# Define a function to run a cell
def run_cell(index, col):
    if cells[index]["type"] == "markdown":
        col.markdown(cells[index]["content"])
    elif cells[index]["type"] == "sql":
        # Execute the SQL code here
        col.text("Executing SQL code...")       
    elif cells[index]["type"] == "ai":
        content = cells[index]["content"]
        for k, v in ai_responses.items():
            if k in content:
                col.markdown(v)
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
        col1, col2 = container.columns([6, 1])

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
            run_cell(i, col1)

        if col2.button(f"Delete", key=f'{i}.2'):
            delete_cell(i)
            st.experimental_rerun()
            break


# Run the app
if __name__ == "__main__":
    app()
