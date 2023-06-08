pergunta4="""

{0}projeto insight
{1}questionario pergunta 4
{0}você teria 20 minutos por dia ? 
{1}===================================================                
{1}0-{0}não soube responder                            
{1}1-{0}sim                                             
{1}2-{0}não{1}                                         
======================================================{0}
""".format('\033[94m','\033[97m')+'\ndigite:\033[97m'

pergunta3="""

{0}projeto insight
{1}questionario pergunta 3
{0}você acha importante ter um professor lhe 
auxiliando nesse processo? 
{1}===================================================                
{1}0-{0}não soube responder                            
{1}1-{0}sim                                             
{1}2-{0}não{1}                                         
======================================================{0}
""".format('\033[94m','\033[97m')+'\ndigite:\033[97m'

pergunta2="""

{0}projeto insight
{1}questionario pergunta 2
{0}você tem codições de aprender o inglês sozinho?
{1}===================================================                
{1}0-{0}não soube responder                            
{1}1-{0}sim                                             
{1}2-{0}não{1}                                         
======================================================{0}
""".format('\033[94m','\033[97m')+'\ndigite:\033[97m'

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
