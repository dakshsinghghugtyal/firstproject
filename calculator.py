import streamlit as st

st.title("calculator")

num1 = st.number_input("enter 1st no.")
num2 = st.number_input("enter 2nd no.")

operation = st.selectbox(
  "choose an operation",
  ["addition", "subtraction", "multiplication", "division"]
)

if st.button("Calculate"):
    if operation == "addition":
        result = num1 + num2

    elif operation == "subtraction":
        result = num1 - num2

    elif operation == "multiplication":
        result = num1 * num2

    elif operation == "division":
        if num2 == 0:
            st.error("Cannot divide by zero!")
        else:
            result = num1 / num2

    if operation != "division" or num2 != 0:
        st.success(f"Result: {result}")

