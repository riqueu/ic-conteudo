import csv
from typing import List

def csv_to_list(arquivo_entrada) -> List:
    """Função que recebe um .csv e retorna uma lista de tuplas com os dados

    Args:
        arquivo_entrada: arquivo .csv de entrada

    Returns:
        List: Lista de tuplas de cada linha do arquivo
    """
    dados_lista = []
    
    with open(arquivo_entrada, 'r', newline='') as arquivo:
        ler_csv = csv.reader(arquivo)
        contador = 1
        for cada_linha in ler_csv:
            # garante que as 4 primeiras linhas serão ignoradas
            if contador > 4:
                dados_lista.append(tuple(cada_linha))
            contador += 1
    return dados_lista

dados = csv_to_list('dados.csv')
print(dados)
