# importar classe
from classes import PontoOnibusLinha
from classes import PontoOnibus
from classes import LinhasOnibus
import pandas as pd

def data_process(filename):
    # definir dados
    _result = {}
    
    
    # ler arquivo de dados
    df = pd.read_csv(filename + ".csv")
    
    
    # listar colunas
    columns = df.columns
    
    for i in range(0, len(df)):
        ponto_onibus = PontoOnibusLinha(df[columns[0]][i], df[columns[1]][i], df[columns[2]][i], df[columns[3]][i], df[columns[4]][i], df[columns[5]][i], df[columns[6]][i], df[columns[7]][i])

        _list_find = _result.get(ponto_onibus.getIdenPonto())
        
        if(_list_find != None):
            _current_linha = LinhasOnibus( ponto_onibus.getCodLinha(), ponto_onibus.getNomeLinha(), ponto_onibus.getNomeSubLinha(), ponto_onibus.getOrigem())
            _list_find.append(_current_linha)
            _result[ponto_onibus.getIdenPonto()] = _list_find

        else:
            _list_linha = []
            _current_linha = LinhasOnibus( ponto_onibus.getCodLinha(), ponto_onibus.getNomeLinha(), ponto_onibus.getNomeSubLinha(), ponto_onibus.getOrigem())
            _list_linha.append(_current_linha)
            _result[ponto_onibus.getIdenPonto()] = _list_linha       

    return _result
        


# ===== Linha principal de execução ====
result_pick = data_process("data")
print("finish")





