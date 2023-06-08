genero="""

{0}projeto insight
{1}genero
{0}digite o genero do entrevistado
{1}===================================================                                           
{1}0-{0}feminino                                             
{1}1-{0}masculino{1}                                         
======================================================{0}
""".format('\033[94m','\033[97m')+'\ndigite:\033[97m'
retorno=['não soube','sim','não']
re_genero=['F','M']

mensagem_erro0='\033[91mdigite um valor numerico entre 0 e 1:\033[0m'
mensagem_erro1='\033[91mdigite um valor numerico entre 0 e 2:\033[0m'
mensagem_erro2='033[91mdigite um valor numerico valido: \033[0m'
chaves=['idade','genero','importância','individualmente','ajuda','tempo']
