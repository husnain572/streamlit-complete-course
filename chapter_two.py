import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Your chai is being brewed")

add_masala=st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your Tea.")

tea_base=st.radio("Pick your chai base:",["Milk","Water","Almond"])
st.write(f"Selected base is {tea_base}.")

tea_flavor=st.selectbox("Choose flavor:",["Adrak","Kesar","Tulsi"])
st.write(f"Selected flavor is {tea_flavor}.")

sugar_level=st.slider("Sugar Level",0,10,5)
st.write(f"Sugar level is {sugar_level}.")

num_cup=st.number_input("How many cups",min_value=1,max_value=10,step=1)
st.write(f"Number of cups: {num_cup}")

name=st.text_input("Enter your name")
if name:
    st.write(f"Welcome {name}!")
    

dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth {dob}")