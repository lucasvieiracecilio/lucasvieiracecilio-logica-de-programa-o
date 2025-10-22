

import streamlit as st

st.title("eai piranha fala quanto quer converte")

dolar = st.number_input("digita ai quanto quer fica pobre mas agora em dolar:",step=2)

reais = dolar * 5.40

st.text(f"o valor do{dolar:.2f}dolares é igual a{reais:.2f}reais.")
