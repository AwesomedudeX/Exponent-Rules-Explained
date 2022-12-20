import streamlit as st
import warnings

warnings.filterwarnings("ignore")

sect = st.sidebar.selectbox("Navigate:", ("The Basics", "Fixed Rules", "Finding Products or Quotients of Powers", "Raising a Product, Quotient or a Power to a Power"))

st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">{sect}</h1>', unsafe_allow_html=True)

if sect == "The Basics":

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">What is a Base?</h2>', unsafe_allow_html=True)
	st.write("A base is the \"main number\" in an expression with only a number and an exponent. This number is used when applying the exponent, and nothing else. For example, if you have ${4^{3}}$ as your exponential expression, 4 would be the base, and the 3 would be the exponent (more on that later). The base doesn't have to be just a single number, though. It can also be an expression inside brackets, like ${(10/2-1)^{3}}$, which would be the same thing as ${4^{3}}$; you'd just do the brackets first - following order of operations (BEDMAS/PEMDAS/GEMS; whatever you want to call it) - and then you'd apply the exponent.")

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">What is an Exponent?</h2>', unsafe_allow_html=True)
	st.write("An exponent is the smaller number that appears to the top-right of your base (see above section). Exponents can be anything, from a decimal, to a fraction, to even an expression, and they can also be stacked on top of one another (we'll discuss the last one in the \"Raising a Product, Quotient or a Power to a Power\"). An exponent is the value that defines how many times your number will be multiplied by itself. An exponent can also be negative (we'll discuss this in \"Fixed Rules\"), though that changes things up a bit. For now, we'll talk about positive exponents. When you raise a number to a power - let's say ${4^{3}}$ from before - you essentially multiply the base by itself for however many times the exponent shows. With ${4^{3}}$, you would do ${4*4*4}$, which would give you an answer of 64. With an expression as an exponent, you might get something like this: ${4^{4*6/8}}$")

if sect == "Fixed Rules":

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Exponent of 1</h2>', unsafe_allow_html=True)
	st.write("")

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Exponent of 0</h2>', unsafe_allow_html=True)
	st.write("")

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Negative Exponents</h2>', unsafe_allow_html=True)
	st.write("")

if sect == "Finding Products or Quotients of Powers":

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Finding Products of a Power</h2>', unsafe_allow_html=True)
	st.write("")

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Finding Quotients of a Power</h2>', unsafe_allow_html=True)
	st.write("")

if sect == "Raising a Product, Quotient or a Power to a Power":

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Raising a Product to a Power</h2>', unsafe_allow_html=True)
	st.write("")
	
	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Raising a Quotient to a Power</h2>', unsafe_allow_html=True)
	st.write("")
	
	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Raising a Power to Another Power</h2>', unsafe_allow_html=True)
	st.write("")
