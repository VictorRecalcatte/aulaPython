import streamlit as st
import random

st.title("Escolher coisas")

aba1, aba2 = st.tabs(['Simples', 'N valores'])

with aba1:
    opcao1 = st.text_input("Insira a opcao 1: ")
    opcao2 = st.text_input("Insira a opcao 2: ")
    opcao3 = st.text_input("Insira a opcao 3: ")

    if st.button("Escolher!"):
        
        lista_de_opcoes = [opcao1, opcao2, opcao3]
        escolha_final = random.choice(lista_de_opcoes)
        st.markdown(f'Sua Escolha foi... {escolha_final}')



with aba2:
    if "lista_n_opcoes" not in st.session_state:
        st.session_state.lista_n_opcoes = []
    
    st.markdown(f'## Opcoes: {st.session_state.lista_n_opcoes}')

    nova_op = st.text_input("Insira uma nova opcao")

    if st.button("Inserir: "):
        st.session_state.lista_n_opcoes.append(nova_op)
        st.rerun()

    if st.button("Apagar Lista "):
        st.session_state.lista_n_opcoes.clear()
        st.rerun()

    if st.button("Escolher!", key="escolher_2"):
        
        escolha_final = random.choice(st.session_state.lista_n_opcoes)
        st.markdown(f'Sua Escolha foi... {escolha_final}')
        
    