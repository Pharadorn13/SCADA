import streamlit as st
import pandas as pd
import sqlite3


st.title('SUNSTAR')
st.subheader("SUNSTAR ENGINEERING THAILAND")

def main():
    st.title('SUNSTAR')
    st.subheader("SUNSTAR ENGINEERING THAILAND")
    menu = ["ALL","MC1"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "ALL":
        st.subheader("ALL MACHINE STATUS")
    else:
        st.subheader("DENKO 1-2")


if __name__ == '__connect__':
    main()
