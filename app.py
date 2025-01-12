import streamlit as st

pg = st.navigation([
    st.Page("pages/update_table.py", title="Update Table", icon=":material/arrow_right:", default=True),
    st.Page("pages/test_run_query.py", title="Test Run Query", icon=":material/arrow_right:"),
])
pg.run()