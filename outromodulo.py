# jeito de importar coisas especificas de um modulo
# from ummodulo import minha_funcao
# minha_funcao() --> acessando quando puxa somente a função

# jeito de importar o modulo inteiro
# import ummodulo
# ummodulo.minha_funcao() --> acessando quando puxa o modulo inteiro

# source <env>/bin/activate --> mac/linux
# source <env>/scripts/activate --> windows

## GIT
# ls -la lista tudo, inclusive os ocultos
# python -m venv .venv --> importar a virtual env e nomea-la como .venv
# which python -- ver qual python ta usando
# source .venv/bin/activate --> ativar a virtual env chamada .venv
# which python -- ver qual python ta usando dn
# pra sair do .venv = desactivate



# ****      passo a passo do django            ****
# mkdir <nome do diretorio>
# cd <nome do diretorio>
# python -m venv .venv --> cria virtualenv
# source .venv/Scripts/activate --> ativar
# pip install -r requirements.txt --> instalar o django que esta no arquivo txt
