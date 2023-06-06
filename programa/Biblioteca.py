from datetime import datetime
class criador_csv:# essa classe é responsavel pela obtenção de dados e criação de um arquivo csv a partir desses dados
    def __init__(self,chaves,nome_arquivo):
        self._nome_arquivo=nome_arquivo
        self._valores=[]
        self._chaves=self._nome_colunas(chaves)

  #esse método recebe os nomes de cada coluna da tabela é cria o documento caso ele não.
    def _nome_colunas(self,chaves):
        self._gerador_csv((','.join(chaves)+',data,hora'),'r')
        return chaves
        

    #esse método cria o csv, além disso ele consegue concatenar todas as entrevistas
    #se os nomes colunas da tabela escrita forém iguais a das colunas da que será escrita

    def _gerador_csv(self,informacao,tipo):
        try:
            with open(self._nome_arquivo+'.csv',tipo,encoding='utf-8') as arquivo:
                if tipo=='r'and arquivo.readline().strip()!=informacao:
                    raise
                elif tipo=='a' or tipo== 'w':
                    arquivo.write(informacao+'\n')
        except: self._gerador_csv(informacao,'w')