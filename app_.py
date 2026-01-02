import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube and fifth power")

n = st.number_input("Enter an Integer", value=1, step=1)

square = n**2
cube = n**3
fifth_power = n**5

st.write(f"Square is {square}")
st.write(f"Cube is {cube}")
st.write(f"Fifth Power is {fifth_power}")