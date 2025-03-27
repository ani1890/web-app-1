import streamlit as st 

st.title("Maths Table creator")
st.text("This App will help to generate tables for any numbers..")
num1 = st.number_input("Enter the number", value=None, step=1)

but1 = st.button("Generate Table")
if but1:
  i = 1
  while i<=10:
    mul = num1 * i
    st.write()
    st.write(num1, "X", i, "=", mul)
    i +=1
st.sidebar.success("You are on Tables page.")
