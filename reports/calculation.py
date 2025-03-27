import streamlit as st
import random

st.title("Maths calculation App")
st.text("This App will perform the mathematical calculations with random nos or manual numbers.")
st.sidebar.success("You are on maths calculation page.")

operation = st.selectbox(
    "Choose Operation to perform",
    ["add", "substract", "multiply", "divide"],
)

if "rand_num1" not in st.session_state:
    st.session_state["rand_num1"] = random.randint(0, 20)

if "rand_num2" not in st.session_state:
    st.session_state["rand_num2"] = random.randint(0, 20)

if st.toggle("Generate my numbers"): # I think this looks nicer than a checkbox here
    if st.button("Next"):
        st.session_state["rand_num1"] = random.randint(0, 20)
        st.session_state["rand_num2"] = random.randint(0, 20)
    num1 = st.session_state["rand_num1"]
    num2 = st.session_state["rand_num2"]
    
    if operation == "add":
      st.write(f"Your random numbers are: `{num1}` + `{num2}`.")
    elif operation == "substract":
      st.write(f"Your random numbers are: `{num1}` - `{num2}`.")
    elif operation == "multiply":
      st.write(f"Your random numbers are: `{num1}` X `{num2}`.")
    elif operation == "divide":
      st.write(f"Your random numbers are: `{num1}` / `{num2}`.")
    ans = st.number_input("Your answer", value=None)
      
    


else:
    num1 = st.number_input(
        "What is the first number?", min_value=0, max_value=20, key="num1"
    )
    num2 = st.number_input(
        "What is the second number?", min_value=0, max_value=20, key="num2"
    )

if st.button("submit"):
    if operation == "add":
        num = num1 + num2
        if num == ans:
          st.success("you are correct!!!")
          st.balloons()
        else:
          st.error("Wrong!!")
    elif operation == "substract":      
        num = num1 - num2
        if num == ans:
          st.success("You are correct!!!")
          st.snow()
        else:
          st.error("Wrong!!")
    elif operation == "multiply":
        num = num1 * num2
        if num == ans:
          st.success("You are correct!!!")
          st.balloons()
        else:
          st.error("Wrong!!")
    elif operation == "divide":
        num = num1 / num2
        if num == ans:
          st.success("You are correct!!!")
          st.snow()
        else:
          st.error("Wrong!!")
          

    st.write(f"Correct answer is {num}.")
