#python -m streamlit run main.py 
import streamlit as st
import sqlite3

# Function to create a database connection
def create_connection():
    conn = sqlite3.connect('panddd.db')
    return conn

# Function to execute a query and fetch results
def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Function to display data in a Streamlit table
def display_data(data):
    st.table(data)

# Main function to run the Streamlit app
def main():
    st.title('SQLite Database Web App')

    # Create a database connection
    conn = create_connection()

    # Query the database (replace with your own query)
    query = 'SELECT * FROM your_table_name'
    result = execute_query(conn, query)

    # Display the data in a Streamlit table
    display_data(result)

# Run the app
if __name__ == '__main__':
    main()
