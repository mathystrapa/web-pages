import pandas as pd
import cgi

form = cgi.FieldStorage()

nome = form.getvalue('name')
zone = form.getvalue('select-zone')
nota = form.getfirst('government-grade')

data = {
    'Nome': [nome],
    'Região': [zone],
    'Nota para o governo': [nota]
}

tabela = pd.DataFrame(data)

print(tabela)