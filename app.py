import streamlit as st
import sqlite3
import pandas as pd

# Create database
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, password text, score integer)''')
conn.commit()

# Signup page
def signup():
    st.title('Signup')
    username = st.text_input('Enter username')
    password = st.text_input('Enter password', type='password')
    if st.button('Signup'):
        c.execute("INSERT INTO users (username, password, score) VALUES (?, ?, ?)", (username, password, 0))
        conn.commit()
        st.success('Account created')

# Login page
def login():
    st.title('Login')
    username = st.text_input('Enter username')
    password = st.text_input('Enter password', type='password')
    if st.button('Login'):
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        if c.fetchone() is not None:
            st.success('Logged in')
        else:
            st.error('Incorrect username or password')

# Leaderboard page
def leaderboard():
    st.title('Leaderboard')
    c.execute("SELECT username, score FROM users ORDER BY score DESC LIMIT 10")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['Username', 'Score'])
    st.table(df)

# Sidebar menu
menu = ['Signup', 'Login', 'Leaderboard']
choice = st.sidebar.selectbox('Select a page', menu)

if choice == 'Signup':
    signup()
elif choice == 'Login':
    login()
elif choice == 'Leaderboard':
    leaderboard()

conn.close()
