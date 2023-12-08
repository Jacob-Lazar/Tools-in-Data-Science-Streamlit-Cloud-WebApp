# Streamlit application
import streamlit as st

def find_maximum_value(number1, number2, number3):
    """
    This function takes three numbers as input and returns the maximum value among them.
    """
    return max(number1, number2, number3)

# Defining the Streamlit app
def app():
    # Seting the title and page layout
    st.set_page_config(page_title='Find the Maximum Value')
    st.title('Find the Maximum Value')

    # Getting user input
    first_number = st.number_input('Enter the first number:', value=0, step=1)
    second_number = st.number_input('Enter the second number:', value=0, step=1)
    third_number = st.number_input('Enter the third number:', value=0, step=1)

    # Computing the result when the user clicks the 'Find Maximum' button
    if st.button('Find Maximum'):
        maximum_value = find_maximum_value(first_number, second_number, third_number)

        # Displaying the result in a success message box
        st.success(f"The maximum value among the given numbers is {maximum_value}.")

if __name__ == '__main__':
    app()
