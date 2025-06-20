from typing import List, Dict
import pandas as pd
import numpy as np

def frequencia_dezenas(dezenas: List[List[int]]) -> pd.Series:
    todas = [d for linha in dezenas for d in linha]
    return pd.Series(todas).value_counts().sort_index()

def repeticoes_pares_impares(dezenas: List[List[int]]) -> Dict[str, float]:
    pares = dezenas[::2]
    impares = dezenas[1::2]
    repeticoes = [len(set(pares[i]) & set(impares[i])) for i in range(min(len(pares), len(impares)))]
    return {
        "media": np.mean(repeticoes),
        "max": np.max(repeticoes),
        "min": np.min(repeticoes)
    }

def dezenas_novas(dezenas: List[List[int]]) -> List[int]:
    novas = [0]
    for i in range(1, len(dezenas)):
        novas.append(len(set(dezenas[i]) - set(dezenas[i-1])))
    return novas

def sugestao_jogo(frequencias: pd.Series, n_top=5, n_low=5, n_mid=5) -> List[int]:
    top = list(frequencias.nlargest(n_top).index)
    low = list(frequencias.nsmallest(n_low).index)
    mid = list(frequencias.sort_values().iloc[len(frequencias)//2 - n_mid//2 : len(frequencias)//2 + n_mid//2].index)
    return sorted((top + low + mid)[:15])