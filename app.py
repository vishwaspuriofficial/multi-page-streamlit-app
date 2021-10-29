import streamlit as st

# Custom imports
from pages import MultiPage
from pages import adding, multiplying

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Multi-page Application")

# Add all your applications (pages) here
app.add_page("Adding", adding.app)
app.add_page("Multipying", multiplying.app)

# The main app
app.run()