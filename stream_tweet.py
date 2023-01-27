import streamlit as st

st.title("Data from Twitter")

keyword= st.text_input("Enter keyword for your search")

number = st.text_input("No. of tweets to be scraped")

start_date = st.text_input("From (Date)")

till_date = st.text_input("To (Date)")

if st.button("upload"):
    st.button("browse")

if st.button("download"):
    data = "data_csv"
    st.write(data)