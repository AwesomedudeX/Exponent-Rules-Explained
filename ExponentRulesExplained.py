import streamlit as st
import warnings

warnings.filterwarnings("ignore")

sect = st.sidebar.selectbox("Navigate:", ("The Basics", "Fixed Rules", "Product, Quotient and Power Rules", "Raising a Product or Quotient to a Power"))

st.header(sect)

if sect == "The Basics":

	st.subheader("What is a Base?")
	st.write("A ")
