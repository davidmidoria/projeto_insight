from datetime import datetime
class criador_csv:# essa classe é responsavel pela obtenção de dados e criação de um arquivo csv a partir desses dados
    def __init__(self,chaves,nome_arquivo):
        self._nome_arquivo=nome_arquivo
        self._valores=[]
        self._chaves=self._nome_colunas(chaves)
        
    #esse método é responsavel por importar a data e hora é fazer o tratamento para um formato mais aceito no Brasil
    @staticmethod
    def _data_e_hora():
        data_hora=str(datetime.today()).split()
        return ('/'.join(data_hora[0].replace('-',' ').split()[::-1]))+','+data_hora[1][:5] # retorna uma string contendo data e hora 

    # esse método retorna um numéro numéro com valor limite podendo ser editavel fora isso ele possui um atributo
    #exececao que se true permite que a função retorne a string '00'
    def _retorna_numeros(self,pergunta,mensagem_erro='erro digite novamente:',limite=1000,exececao=False):
        try:
            valor=input(pergunta)
            valor=(valor if valor=='00'and exececao==True else int(valor) )
        except:valor=limite+1
        return (valor if int(valor)<=limite else self._retorna_numeros(mensagem_erro))
    
    
    # esse método permite armazenar numeros na lista de valores fora isso retorna true a cada número novo armazenado
    # ele pode abrir uma execeção para caso o cliente digite '00' retornando assim o valor False, para habilitar essa
    #função basta dar como argumento para o atributo exececao o valor True
    def armazena_numeros(self,pergunta,mensagem_erro,limite=1000,exececao=False):
        valor=self._retorna_numeros(pergunta,mensagem_erro,limite,exececao)
        if valor=='00':
            return False
        else:
           self._valores.append(str(valor))
           return True 
        
    #esse método deve receber um pergunta cujas opções devem ser respondidas a partir de valores númericos começando
    #do 0, esse método possui um atributo retorno que deve receber uma lista com valores, que a partir da resposta do
    #cliente um sera devolvido, por exemplo  sé o cliente retorna o número um, o indice de indexação número um da 
    #lista sera devolvido OBS:(o item número um não é o primeiro item esse é o 0, o item de indexação 1 seria o segundo
    # item)
    def _retorna_resposta(self,pergunta,retorno,mensagem_erro):
        return retorno[self._retorna_numeros(pergunta,mensagem_erro,limite=(len(retorno)-1))]
    
    
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
<<<<<<< HEAD
        
    #esse método deve receber uma lista contendo as perguntas e uma lista com as respostas que serão armazenadas
    #no atributo __valores segundo a resposta do usuario 
    def armazena_valores_nao_num(self,perguntas,retorno,mensagem_erro):
            self._valores.extend([self._retorna_resposta(pergunta,retorno,mensagem_erro)for pergunta in perguntas])

    #esse método transforma as respostas em uma string é armazena no atributo __total valores  
    def salvar_dados(self):
        if len(self._chaves)==len(self._valores):
            self._gerador_csv((','.join(self._valores)+','+self._data_e_hora()),'a')
            self._valores=[]

#   
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
                elif tipo=='a' or 'w':
                    arquivo.write(informacao+'\n')
        except: self._gerador_csv(informacao,'w')
=======
>>>>>>> b5e1113ad0c3c6760bcd578dd497aa0616350ce3
