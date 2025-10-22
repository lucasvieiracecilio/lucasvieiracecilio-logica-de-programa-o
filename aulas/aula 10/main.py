import streamlit as st

lista_usuarios = []

st.title("gerenciador de tarefas")
nome = st.text_input("nome", placeholder = "digite seu nome")

idade = st.number_input("idade", placeholder = "digite sua idade",step = 1)

task = st.checkbox("estou indo para a cademia toda semana")

cor = st.color_picker("escolha sua cor favorita")

main_do_vavas = st.selectbox("escolha um personagem",["jett","sage","rase","brim","reyna","outros"])

on = st.toggle("ligas a putaria")
print(on)

if (on):
    st.write("putaria ta ligada")
else:
    st.write("modo ta na bed")
print(cor)

botao = st.button("enviar")
if botao:
    st.write("clicaru no botaoinho hummmm")
else:
    st.write("num clicaru")


# st.title("Formulario")


# nome = st.text_input("nome",
# placeholder = "digite seu nome")

# idade = st.number_input("idade", placeholder = "digite sua idade", step = 1)

# task = st.checkbox("estou estudando em casa")

# cor = st.color_picker("escolha uma cor")

# stacks = st.selectbox("escolha as stacks",["backEnd","frontEnd","fullstack","estagiario"])

# on = st.toggle("ligar")
# print(on)

# if (on) :
#     st.write("modo dark")
# else:
#     st.write("modo light")
# print(cor)

# botao = st.button("enviar",type="primary")
# if botao:
#     st.write("fui clicado")
# else:
#     st.write("nao fui")





# import streamlit as st 


# st.title("toma na sua ku")
# st.header("cabeçario principal", divider=True)

# st.text("ola mundo")

# nome = st.text_input("digite seu nome:")
# idade = st.number_input("digite sua idade:",step=1)