import streamlit as st
import calendar

st.set_page_config(
    page_title="Planorama",
    page_icon="calendar.png",
    menu_items={
        "About":"""Welcome to Planorama, the ultimate calendar experience. View and manage your dates with our sleek and intuitive interface, tailored for seamless year and month exploration."""
    }
)

st.write("<h2 style='color:#FF7F50';>Your Personalized Calendar at a Glance</h2>",unsafe_allow_html=True)

col1,col2=st.tabs(["Yearly Calendar","Monthly Calendar"])

calendar.setfirstweekday(calendar.SUNDAY)

with col1:
    year=st.number_input(label="Enter a Year",format="%d",min_value=0,key=0)
    button=st.button(label="Generate",key=1)
    if button:
        st.text(calendar.calendar(year))

with col2:
    year=st.number_input(label="Enter a Year",format="%d",step=1,key=2)
    month=st.number_input(label="Enter a Month",format="%d",min_value=1,help="enter month value between 1 to 12")
    button=st.button(label="Generate",key=3)
    if button:
        try:
            st.text(calendar.month(year,month))
        except:
            st.error("Invalid Month!")