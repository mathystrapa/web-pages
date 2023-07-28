#front-end
    #HTML, CSS e JavaScript

#back-end
    #python

#framework: flask (instalado em ambiente virtual - essencial para quando for subir o site pro servidor)


# CRIAR SITES EM PYTHON:

    # 1) IMPORTAR O Flask
    # 2) CRIAR APLICATIVO -> app = Flask(__name__)
    # 3) CRIAR PRIMEIRA ROTA/PÁGINA -> @app.route('/')
    # 4) DEFINIR FUNÇÃO PRA HOMEPAGE -> def função_home_page()   *TEM QUE SER DEPOIS DA CRIAÇÃO DA ROTA
                                          # return(coisa)
    # 5) RODAR O APLICATIVO -> app.run()

from flask import Flask, render_template

app = Flask(__name__)   # criando app

@app.route('/')   # decorator

def Home():
    return render_template('index.html')   # abre o arquivo index.html na homepage (primeira rota) do site

app.run()