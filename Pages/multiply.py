import streamlit as st

def app():
    st.header('Multiplying Numbers')

    st.subheader("Made by Vishwas Puri using Streamlit (python)")

    num1 = st.number_input('Enter Number 1:')
    num2 = st.number_input('Enter Number 2:')

    st.write(f"The product is: {num1 * num2}")
