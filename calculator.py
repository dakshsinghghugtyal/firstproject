import streamlit as st

st.title("CALCULATOR")

num1 = st.number_input("enter 1st no.")
num2 = st.number_input("enter 2nd no.")

operation = st.selectbox(
  "choose an operation",
  ["ADDITION", "SUBTRACTION", "MULTIPLICATION", "DIVISION"]
)

if st.button("Calculate"):
    if operation == "ADDITION":
        result = num1 + num2

    elif operation == "SUBTRACTION":
        result = num1 - num2

    elif operation == "MULTIPLICATION":
        result = num1 * num2

    elif operation == "DIVISION":
        if num2 == 0:
            st.error("Cannot divide by zero!")
        else:
            result = num1 / num2

    if operation != "DIVISION" or num2 != 0:
        st.success(f"Result: {result}")

