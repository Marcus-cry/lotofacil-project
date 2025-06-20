import matplotlib.pyplot as plt
import pandas as pd

def plotar_frequencias(frequencias: pd.Series):
    plt.figure(figsize=(12, 6))
    frequencias.plot(kind='bar', color='skyblue')
    plt.title('Frequência das Dezenas')
    plt.xlabel('Dezena')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.tight_layout()
    plt.show()