import sqlite3
import streamlit as st
import pandas as pd

# Hardcoded username and password for login (you can change these values)
USERNAME = "KAVIN"
PASSWORD = "2004"

# Create a login function
def login(username, password):
    if username == USERNAME and password == PASSWORD:
        return True
    else:
        return False

# Display login form
st.title("Login")

# Input fields for username and password
input_username = st.text_input("Username")
input_password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    if login(input_username, input_password):
        st.success("Login successful!")
        
        # Connect to SQLite database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Create a table with additional fields if it doesn't exist (optional, for first-time setup)
        c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            phone_number TEXT,
            email TEXT,
            location TEXT,
            work_type TEXT,
            worker_name TEXT
        )
        ''')
        conn.commit()

        # Display stored data
        st.title("Stored User Data")

        # Fetch all data from the database
        c.execute('SELECT * FROM users')
        data = c.fetchall()

        if data:
            # Convert data to a Pandas DataFrame for better display
            df = pd.DataFrame(data, columns=['S.No', 'Name', 'Age', 'Phone Number', 'Email', 'Location', 'Type of Work', 'Worker Name'])
            
            # Display the DataFrame as a table in Streamlit
            st.table(df)
        else:
            st.write("No data available.")

        # Close the connection
        conn.close()
    else:
        st.error("Invalid username or password!")
