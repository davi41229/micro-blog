from app import app #do pacote app importe da variavel app
from flask import render_template
@app.route('/') #rota principal(homepage) a diretiva ou raiz
@app.route('/index') # rota /index

def index(): #funçao com o que vai ser exibido
	return render_template('index.html') #carregar o html dentro da pasta templates

@app.route('/contato')
def contato():
	return render_template('contato.html')	