from flask import Flask, render_template, request
import requests
from main import check_cep

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
     
     # Check if method is POST
    if request.method == 'POST':
        cep = request.form['cep']
        
        # Check if cep is bigger than 8 or smaller than 8.
        validate, aviso = check_cep(cep)

        if validate == False:
            return render_template('index.html', aviso=aviso, port=False)
    
        #  Requests cep API
        info_tot = ''
        port = True
        r = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
        info_tot = r.json()
        r = str(r)
        
        # if cep is not found
        if r  == '<Response [404]>':
            aviso = 'CEP não encontrado!'
            return render_template('index.html', aviso=aviso)
        
        # Defined variables to show in the template
        rua = info_tot['address']
        bairro = info_tot['district']
        uf = info_tot['state']
        city = info_tot['city']
        info = info_tot['cep']

        return render_template('index.html', cep=cep, rua=rua, bairro=bairro, uf=uf, city=city, info=info, port=port) 

    aviso = 'Digite o CEP sem -'
    return render_template('index.html', aviso=aviso)