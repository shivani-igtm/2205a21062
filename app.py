
import streamlit as st

def Elec_Para(V, R, T):
    I = V / R
    P = I ** 2 * R
    H = I ** 2 * R * T
    return I, P, H

st.title("2205A21062 ps1")

st.text("Calculate current, power, and heat energy based on voltage, resistance, and time.")

col1, col2 = st.columns(2)

with col1:
    with st.container():
        V = st.number_input("Voltage (V)", value=10.0)
        R = st.number_input("Resistance (Ω)", value=1.0)
        T = st.number_input("Time (s)", value=1.0)
        compute = st.button("Compute")

with col2:
    with st.container():
        if compute:
            I, P, H = Elec_Para(V, R, T)
            st.write(f"load current(I) = {I:.2f} A")
            st.write(f"load power(P) = {P:.2f} W")
            st.write(f"Heat Energy (H) = {H:.2f} wh")

