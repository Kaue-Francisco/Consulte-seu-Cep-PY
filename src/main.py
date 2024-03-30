from routes import *

def main():
    app.run()

def check_cep(cep):
    """
        Check if the user entered the correct amount of numbers.
    """

    # Check if cep is bigger than 8 or smaller than 8.
    if len(cep) > 8 or len(cep) < 8 and len(cep) != 0:
            aviso = 'O CEP é composto por 8 números.'
            return False, aviso
        
    # Check different from 0.
    elif len(cep) == 0:
        aviso = 'Digite o CEP sem -'
        return False, aviso
    
    return True, None
    

if __name__ == "__main__":
    main()