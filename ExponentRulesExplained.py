import streamlit as st
import warnings

warnings.filterwarnings("ignore")

sect = st.sidebar.selectbox("Navigate:", ("The Basics", "Fixed Rules", "Finding Products or Quotients of Powers", "Raising a Product, Quotient or a Power to a Power"))

st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">{sect}</h1>', unsafe_allow_html=True)

if sect == "The Basics":

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">What is a Base?</h2>', unsafe_allow_html=True)
	st.write("A base is the \"main number\" in an expression with only a number and an exponent. This number is used when applying the exponent, and nothing else. For example, if you have ${4^3}$ as your exponential expression, 4 would be the base, and the 3 would be the exponent (more on that later). The base doesn't have to be just a single number, though. It can also be an expression inside brackets, like ${(10/2-1)^3}$, which would be the same thing as ${4^3}$; you'd just do the brackets first - following order of operations (BEDMAS/PEMDAS/GEMS; whatever you want to call it) - and then you'd apply the exponent.")

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">What is an Exponent?</h2>', unsafe_allow_html=True)
	st.write("An exponent is the smaller number that appears to the top-right of your base (see above section). Exponents can be anything, from a decimal, to a fraction (we won't talk about those last 2 here, since it's a more advanced concept), to even an expression, and they can also be stacked on top of one another (we'll discuss the last one in the \"Raising a Product, Quotient or a Power to a Power\"). An exponent is the value that defines how many times your number will be multiplied by itself. An exponent can also be negative (we'll discuss this in \"Fixed Rules\"), though that changes things up a bit. For now, we'll talk about positive exponents. When you raise a number to a power - let's say ${4^3}$ from before - you essentially multiply the base by itself for however many times the exponent shows. With ${4^3}$, you would do ${4*4*4}$, which would give you an answer of 64. With an expression as an exponent, you might get something like this: ${4^{4*6/8}}$. In this situation, you'd simply just do the exponential expression first, which would give you a result of 3, and then raise 4 (your base) to that power, which gets you the same answer as just using 3 itself; 64. It doesn't matter what your exponent is; if it's a positive integer, either on its own or as the result of an expression, you'd just multiply your base by itself for the amount of times that the exponent shows.")

if sect == "Fixed Rules":

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Exponent of 1</h2>', unsafe_allow_html=True)
	st.write("Having an exponent of 1 is really simple. Just as you'd multiply 3 by itself twice (${3*3}$) if you had ${3^2}$, you'd just take 3 on its own if you had ${3^1}$. In other words, any number raised to the power of 1 is equal to that base. Every number has this property, no matter what it is, and even if it's not shown, every number technically has this property; it just seems really unnecessary to put it down because it's a waste of space. The only times you'd ever put this exponent down would be to show your reasoning. Otherwise, in practical math, this exponent has no use whatsoever.")

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Exponent of 0</h2>', unsafe_allow_html=True)
	st.write("Any number raised to an exponent of 0 automatically equals 1. Think of it like this; a cube with side lengths of 3 units would be equal to ${3^3}$, or 3 cubed. The power acts as the number of \"dimensions\" of your hypothetical shape, just as ${3^2}$ would be equal to 3 squared - this would create a square with the same side lengths, but since the exponent is 2 instead of 3, we'd take a 2D shape instead of a 3D shape. Now, once we get to 1D, we just have the number itself, which would be what we discussed in the previous section (see \"Exponent of 1\"). What happens, then, when we have an exponent of 0? just as a cubed value forms a cube, a squared value forms a square, and a single value forms a line, an undefined dimensional value would simply form a point. This point has no dimensions, and therefore its value is 1. It can't be 0, because it exists, and 0 is a value used to describe nonexistent things. This means that its value must be a single unit. If you find that confusing, just think of it as dividing the number by itself every time you reduce the power, to the point where you're dividing the base raised to the power of 1 by itself, which would give you 1. Just like these examples, whenever you have a number raised to the power of 0 - whether it's positive, negative or 0 - that number always becomes 1. The same goes for having an expression as the base. Whatever that result is, it would just become 1. Don't bother doing the math. If it's in brackets, and you have a 0 in superscript (shrunk and in the top-right) right after it, the result is 1.")

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
