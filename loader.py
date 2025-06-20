import pandas as pd

def carregar_dados(caminho_arquivo: str) -> pd.DataFrame:
    df = pd.read_csv(caminho_arquivo)
    df.columns = df.columns.str.strip().str.lower()
    return df