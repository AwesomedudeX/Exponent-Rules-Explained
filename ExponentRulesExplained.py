import streamlit as st
import warnings

warnings.filterwarnings("ignore")

sect = st.sidebar.selectbox("Navigate:", ("The Basics", "Fixed Rules", "Finding Products or Quotients of Powers With Like Bases", "Raising a Product, Quotient or a Power to a Power"))

st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">{sect}</h1>', unsafe_allow_html=True)

if sect == "The Basics":

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">What is a Base?</h2>', unsafe_allow_html=True)
	st.write("A base is the \"main number\" in an expression with only a number and an exponent. This number is used when applying the exponent, and nothing else. For example, if you have $4^3$ as your exponential expression, 4 would be the base, and the 3 would be the exponent (more on that later). The base doesn't have to be just a single number, though. It can also be an expression inside brackets, like $(10/2-1)^3$, which would be the same thing as $4^3$; you'd just do the brackets first - following order of operations (BEDMAS/PEMDAS/GEMS; whatever you want to call it) - and then you'd apply the exponent.")

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">What is an Exponent?</h2>', unsafe_allow_html=True)
	st.write("An exponent is the smaller number that appears to the top-right of your base (see above section). Exponents can be anything, from a decimal, to a fraction (we won't talk about those 2 here, since it's a more advanced concept), to even an expression, and they can also be stacked on top of one another (we'll discuss the last one in the \"Raising a Product, Quotient or a Power to a Power\"). An exponent is the value that defines how many times your number will be multiplied by itself. An exponent can also be negative (we'll discuss this in \"Fixed Rules\"), though that changes things up a bit. For now, we'll talk about positive exponents. When you raise a number to a power - let's say $4^3$ from before - you essentially multiply the base by itself for however many times the exponent shows. With $4^3$, you would do $4*4*4$, which would give you an answer of 64. With an expression as an exponent, you might get something like this: $4^{4*6/8}$. In this situation, you'd simply just do the exponential expression first, which would give you a result of 3, and then raise 4 (your base) to that power, which gets you the same answer as just using 3 itself; 64. It doesn't matter what your exponent is; if it's a positive integer, either on its own or as the result of an expression, you'd just multiply your base by itself for the amount of times that the exponent shows.")

if sect == "Fixed Rules":

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Exponent of 1</h2>', unsafe_allow_html=True)
	st.write("Having an exponent of 1 is really simple. Just as you'd multiply 3 by itself twice ($3*3$) if you had $3^2$, you'd just take 3 on its own if you had $3^1$. In other words, any number raised to the power of 1 is equal to itself. Every number has this property, no matter what it is, and even if it's not shown, every number technically has this property; it just seems really unnecessary to put it down because it's a waste of space. The only times you'd ever put this exponent down would be to show your reasoning. Otherwise, in practical math, this exponent has no use whatsoever.")

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Exponent of 0</h2>', unsafe_allow_html=True)
	st.write("Any number raised to an exponent of 0 automatically equals 1. Think of it like this; a cube with side lengths of 3 units would be equal to $3^3$, or 3 cubed. The power acts as the number of \"dimensions\" of your hypothetical shape, just as $3^2$ would be equal to 3 squared - this would create a hypothetical square with the same side lengths as the cube, but since the exponent is 2 instead of 3, we'd take a 2D shape instead of a 3D shape. Now, once we get to 1D, we just have the number itself, which would be what we discussed in the previous section (see \"Exponent of 1\"). What happens, then, when we have an exponent of 0? Just as a cubed value forms a cube, a squared value forms a square, and a single value forms a line, an undefined dimensional value would simply form a point. This point has no dimensions, and therefore its value is 1. It can't be 0, because it exists, and 0 is a value used to describe nonexistent things. This means that its value must be a single unit. If you find that confusing, just think of it as dividing the number by itself every time you reduce the power, to the point where you're dividing the base raised to the power of 1 by itself, which would give you 1. Just like these examples, whenever you have a number raised to the power of 0 - whether it's positive, negative or 0 - that number always becomes 1. The same goes for having an expression as the base. Whatever that result is, it would just become 1. Don't bother doing the math. If it's in brackets, and you have a 0 in superscript (shrunk and in the top-right) right after it, the result is 1.")

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Negative Exponents</h2>', unsafe_allow_html=True)
	st.write("A negative exponent can only be described as a fraction of a power of the base. Think of it like this: when you increase the power of a number by 1, the result will multiply by the base. The reverse would be to divide by the base, so $3^1$ is 3 (see \"Exponent of 1\"), and $3^0$ is 1 (see \"Exponent of 0\"), which would mean $3^{-1}$ is 1/3 of that; 3^{-1}} is 1/3. This would mean that $3^{-2}$ would be 1/9, and $3^{-3}$ would be 1/27. At this point, you can hopefully see the pattern here. The negative powers of a number are just 1 over the positive of that power; $2^{(-5)}$ = $1/2^{5}$. Whenever a number has a negative power attached to it, the result is 1 over whatever the result would be if the exponent was positive.")

if sect == "Finding Products or Quotients of Powers With Like Bases":

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Finding Products of a Power With Like Bases</h2>', unsafe_allow_html=True)
	st.write("When you have 2 exponential values with the same base, and you want to find out their product, all you have to do is one thing; add. When you have 2 exponential values with the same base in the same multiplication expression, it's like multiplying a number by itself a certain amount of times, and multiplying that by the same number, with the second number also being multiplied by itself a certain amount of times. Since you're just multiplying the same number over and over again, you can just add the exponents and keep the base the same; when you have $2^2+2^5$, you can just add the exponents (2 and 5), which would give you your final answer; $2^7$.")

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Finding Quotients of a Power With Like Base</h2>', unsafe_allow_html=True)
	st.write("Just as we discussed finding quotients of a power in the previous section, here, we'll discuss the inverse of that; finding quotients of powers with the same bases. Doing this is quite simple. All you need to do, is just take the exponent of the second power, and subtract it from the exponent of the first power. Whether it's positive, negative or 0 (see \"Fixed Rules\"), you just simply subtract, and whatever the resulting power is would be your answer. For example, if you take $4^2/4^5$, then you'd just have to subtract the 5 from the 2, which would give you -3. This would leave you with a result of $4^{(-3)}$, or 1/64.")

if sect == "Raising a Product, Quotient or a Power to a Power":

	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Raising a Product to a Power</h2>', unsafe_allow_html=True)
	st.write("")
	
	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Raising a Quotient to a Power</h2>', unsafe_allow_html=True)
	st.write("")
	
	st.markdown(f'<h2 style="color:#FFAA00;font-size:25px;">Raising a Power to Another Power</h2>', unsafe_allow_html=True)
	st.write("")
