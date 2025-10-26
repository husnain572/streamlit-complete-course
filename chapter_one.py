import streamlit as st

st.title("Hello Streamlit APP")
st.subheader("Built for AI and Data Learners")
st.text("Welcome to your first interactive Streamlit app.")
st.write("Choose what you want to explore today!")
option=st.selectbox("Select Topic",["Machine Learning","Deep Learning","Computer Vision","Natural Language Processing","Data Analytics"])
st.write(f"You selected: ***{option}***")
st.divider()
st.write("### Streamlit Message Examples:")
st.success("This is a *success* message — used for confirmations.")
st.warning("This is a *warning* message — used for potential issues.")
st.error("This is an *error* message — used for critical alerts.")
st.error("This is an *error* message — used for critical alerts.")
