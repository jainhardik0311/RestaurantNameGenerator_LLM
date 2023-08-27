import streamlit as st
import setup

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Australian"))

if cuisine:
    response = setup.generate_restaurant_name_and_items(cuisine)

    st.header(response['restaurant_name'].strip())
    st.subheader(response['restaurant_desc'])

    menu_items = response['menu_items'].strip().split(",")

    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)