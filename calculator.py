import streamlit as st

def main():
    st.title("Simple Calculator")

    # Input fields for numbers
    num1 = st.number_input("Enter the first number", format="%.2f")
    num2 = st.number_input("Enter the second number", format="%.2f")

    # Dropdown for selecting operation
    operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Perform the calculation
    result = None
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Division by zero is not allowed.")
    
    # Display the result
    if result is not None:
        st.write(f"The result of {operation.lower()}ing {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
