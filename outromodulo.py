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
    # echo "django" >> requirements.txt
# pip install -r requirements.txt --> instalar o django que esta no arquivo txt

# django-admin startproject salada .  --> iniciar o django, criar um projeto django 
# python manage.py startapp tempero --> criar uma aplicação django


# MVC
# M = model - cria as coisas que vão ser salvas no banco de dados (SGBG - Sistema gerenciador de banco de dados que realmente é o banco de dados)
# V = view - aonde são construidas as páginas (regra de negócio)
# C - controlls - lógica de negocio
# MTV - tudo dentro de tempero
# M - model - comunica com o banco de dados (vai estar na = models.py)
# T - templates - páginas (html) (vai estar na = templates/)
# V - view - lógico de negócio (vai estar na = views.py)


## proximos passos git
# python manage.py migrate
# python manage.py runserver
