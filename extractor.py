from typing import List
import pandas as pd

def extrair_dezenas(df: pd.DataFrame) -> List[List[int]]:
    return df[[f'd{i}' for i in range(1, 16)]].values.tolist()