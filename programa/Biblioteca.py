from datetime import datetime
class criador_csv:# essa classe é responsavel pela obtenção de dados e criação de um arquivo csv a partir desses dados
    def __init__(self,chaves,nome_arquivo):
        self._nome_arquivo=nome_arquivo
        self._valores=[]
        self._chaves=self._nome_colunas(chaves)