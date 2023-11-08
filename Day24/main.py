import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/1.png", width=300)

with col2:
    st.title("Ardit Sulce")
    content = """
    grwwfdsfsdf
    """
    st.info(content)

content2 = """
    grwwfdsfsdfsdgsdvsdgsgdsgsdgasgfgdsggfdgdfdhhfhdfsdfgsgdsgsdagsdg
    """
st.write(content2)
# can use st.info(content)
col3, empty_col, col4, empty_col, col5 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=",")
with col3:
    for index, row in df[:4].iterrows():
        st.header(row["first name"])
        st.write(row["role"])
        st.image("images/" + row["image"])
with col4:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"])
        st.write(row["role"])
        st.image("images/" + row["image"])
with col5:
    for index, row in df[8:].iterrows():
        st.header(row["first name"])
        st.write(row["role"])
        st.image("images/" + row["image"])
