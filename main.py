# importar classe
from classes import PontoOnibus
import pandas as pd

def data_process(filename):
    # ler arquivo de dados
    df = pd.read_csv(filename + ".csv")
    
    # Lista de pontos
    list_pontos = []
    
    # Definir lista de colunas
    columns = df.columns
    
    for i in range(0, len(df)):
        ponto_onibus = PontoOnibus(df[columns[0]][i], df[columns[1]][i], df[columns[2]][i], df[columns[3]][i], df[columns[4]][i], df[columns[5]][i], df[columns[6]][i], df[columns[7]][i])
        list_pontos.append(ponto_onibus)
    
    return list_pontos
    
    


# ===== Linha principal de execução ====
data_process("data")





