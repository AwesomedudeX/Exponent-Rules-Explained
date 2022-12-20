import streamlit as st
import warnings

warnings.filterwarnings("ignore")

sect = st.sidebar.selectbox("Navigate:", ("The Basics", "Fixed Rules", "Product, Quotient and Power Rules", "Raising a Product or Quotient to a Power"))

st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">{sect}</h1>', unsafe_allow_html=True)

if sect == "The Basics":

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">What is a Base?</h2>', unsafe_allow_html=True)
	st.write("A base is the \"main number\" in an expression with only a number and an exponent. This number is used when applying the exponent, and nothing else. For example, if you have $\mathregular{4^{3}}$, 4 would be the base, and the 3 would be the exponent (more on that later). The base doesn't have to be just a single number, though. It can also be an expression inside brackets")
