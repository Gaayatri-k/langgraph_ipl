import streamlit as st
from graph import app
st.title(" IPL Assistant")
query = st.text_input("Ask IPL Question")
if st.button("Submit"):
    result = app.invoke({
        "query": query
    })
    st.write(result["answer"])