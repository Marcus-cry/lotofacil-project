import streamlit as st
import pandas as pd
import numpy as np
from utils.extractor import extrair_dezenas
from utils.stats import (
    frequencia_dezenas, repeticoes_pares_impares, dezenas_novas,
    sugestao_jogo
)

st.set_page_config(page_title="Análise da Lotofácil", layout="centered")
st.title("🔍 Análise Estatística da Lotofácil")

uploaded_file = st.file_uploader("Envie o arquivo CSV dos concursos (ex: lotofacil.csv)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    dezenas = extrair_dezenas(df)

    freq = frequencia_dezenas(dezenas)
    repeticoes = repeticoes_pares_impares(dezenas)
    novas = dezenas_novas(dezenas)

    st.subheader("📊 Frequência das Dezenas")
    st.bar_chart(freq)

    st.subheader("🔁 Repetições entre concursos pares e ímpares")
    st.write(repeticoes)

    st.subheader("📈 Novas dezenas por concurso")
    st.line_chart(novas)

    st.subheader("🎯 Sugestão de Jogo Estatístico")
    jogo = sugestao_jogo(freq)
    st.success(f"Jogo sugerido: {jogo}")
else:
    st.info("Aguardando envio de arquivo .csv com os concursos.")