#comandos iniciais para o flask
from flask import Flask #classe flask
app = Flask(__name__) # criar a variavel app e instancia-la com o parametro __name__

from app import routes #da pasta app importando o arquivo routes
