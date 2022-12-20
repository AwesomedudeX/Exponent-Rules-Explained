import streamlit as st
import warnings

warnings.filterwarnings("ignore")

sect = st.sidebar.selectbox("Navigate:", ("The Basics", "Fixed Rules", "Product, Quotient and Power Rules", "Raising a Product or Quotient to a Power"))

st.markdown(f'<h1 style="color:#FF0000;font-size:25px;">{sect}</h1>', unsafe_allow_html=True)

if sect == "The Basics":

	st.markdown(f'<h2 style="color:#FFFF00;font-size:25px;">What is a Base?</h2>', unsafe_allow_html=True)
	st.write("A ")
