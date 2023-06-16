from Biblioteca import criador_csv
from conteudo import *

# inicialização do arquivo
objeto_csv=criador_csv(chaves,'projeto_insght')
loop_secundario=True
while loop_secundario==True:
    
    loop_secundario=objeto_csv.armazena_numeros(idade,mensagem_erro2,limite=123,exececao=True)
    if loop_secundario==True: 
        objeto_csv.armazena_valores_nao_num([genero],re_genero,mensagem_erro0)
        objeto_csv.armazena_valores_nao_num(perguntas,retorno,mensagem_erro1)
        objeto_csv.salvar_dados()