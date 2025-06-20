from utils.loader import carregar_dados
from utils.extractor import extrair_dezenas
from utils.stats import frequencia_dezenas, repeticoes_pares_impares, dezenas_novas, padroes_distribuicao, sugestao_jogo
from utils.visual import plotar_frequencias
import numpy as np

def main():
    caminho_csv = 'data/lotofacil.csv'
    df = carregar_dados(caminho_csv)
    dezenas = extrair_dezenas(df)

    freq = frequencia_dezenas(dezenas)
    repeticoes = repeticoes_pares_impares(dezenas)
    novas = dezenas_novas(dezenas)
    padroes = padroes_distribuicao(dezenas)

    print("\n===== Estatísticas Gerais =====")
    print("Repetições entre Pares e Ímpares:", repeticoes)
    print("Média de dezenas novas por concurso:", round(np.mean(novas), 2))

    print("\n===== Frequência das Dezenas =====")
    print(freq)
    plotar_frequencias(freq)

    print("\n===== Sugestão de Jogo =====")
    jogo_sugerido = sugestao_jogo(freq)
    print("Jogo sugerido:", jogo_sugerido)

if __name__ == "__main__":
    main()