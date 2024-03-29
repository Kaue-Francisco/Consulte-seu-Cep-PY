import requests
from flask import Flask, render_template, request
cep = ''

# Abre a rota index do site
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
     
     # Verefica se o método é POST
    if request.method == 'POST':
        cep = request.form['cep']
        
        # Verefica a quantidade de número o Usuário digitou
        if len(cep) > 8 or len(cep) < 8 and len(cep) != 0:
            port = False
            aviso = 'O CEP é composto por 8 números.'
            return render_template('index.html', aviso=aviso)
        
        elif len(cep) == 0:
            port = False
            aviso = 'Digite o CEP sem -'
            return render_template('index.html', aviso=aviso)
    
        # Processo de fazer a consulta na API
        elif len(cep) == 8:
            info_tot = ''
            cep = request.form['cep']
            port = True
            r = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
            info_tot = r.json()
            r = str(r)
            
            #Vereficar se a consulta é válida ou não
            if r  == '<Response [404]>':
                aviso = 'CEP não encontrado!'
                return render_template('index.html', aviso=aviso)
            else:
                rua = info_tot['address']
                bairro = info_tot['district']
                uf = info_tot['state']
                city = info_tot['city']
                info = info_tot['cep']
                return render_template('index.html', cep=cep, rua=rua, bairro=bairro, uf=uf, city=city, info=info, port=port) 
    
    # Vereficar se o usuário digitou nada
    else:
        aviso = 'Digite o CEP sem -'
        return render_template('index.html', aviso=aviso)
    

if __name__ == "__main__":
    app.run()