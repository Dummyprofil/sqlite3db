import streamlit as st
import sqlite3

# Create a connection to SQLite database
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# Create a table to store user data if it doesn't exist already
c.execute('''CREATE TABLE IF NOT EXISTS users (name TEXT)''')

# Streamlit app
def main():
    st.title("Welcome to the Name Storing App")
    
    # Ask for the user's name
    name = st.text_input("Please enter your name:")
    
    # Store the user's name in the database when the button is clicked
    if st.button("Submit"):
        c.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        st.success("Your name has been successfully stored!")
    
    # Show a greeting message with the user's name
    if st.button("Greet Me"):
        c.execute("SELECT name FROM users")
        result = c.fetchone()
        if result:
            st.write("Hello, {}!".format(result[0]))
        else:
            st.warning("No name has been stored yet.")

if __name__ == "__main__":
    main()
