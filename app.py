import random
import streamlit as st

st.set_page_config(page_title="Globo Lotofácil", page_icon="🎱")

st.title("Simulador de Sorteio - Lotofácil")

if st.button("Sortear 15 números"):
    sorteados = random.sample(range(1, 26), 15)
    sorteados.sort()
    st.success("Números sorteados:")
    cols = st.columns(5)
    for idx, num in enumerate(sorteados):
        cols[idx % 5].markdown(f"## {num:02d}")
