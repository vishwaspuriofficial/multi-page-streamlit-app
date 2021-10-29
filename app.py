import streamlit as st

# Custom imports
from pages import MultiPage
from Pages import add, multiply

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Multi-page Application")

# Add all your applications (pages) here
app.add_page("Adding", add.app)
app.add_page("Multipying", multiply.app)

# The main app
app.run()