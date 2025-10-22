import streamlit as st

st.title("convertor em IMC")
peso= st.number_input("digite seu peso:",step=1)
altura= st.number_input("digite sua altura",min_value=0.1)

imc= peso / altura**2

st.text(f"o seu peso é igual{imc:.2f}")