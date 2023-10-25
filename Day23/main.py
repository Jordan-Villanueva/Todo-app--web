import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

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