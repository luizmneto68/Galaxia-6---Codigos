

class Empresa:

    def __init__(self, name, ticker): # construtor (parametros do construtor)

        self.name_emp = name # parâmetroa do construtor sendo atribuido ao atributos da instancia 
        self.ticker_emp = ticker
        
        

# isso aqui serve para fazer testes dentro do próprio código. Só vai rodar quando rodar esse código como main
if __name__ == "__main__": 

    empresa_de_motor = Empresa(name = "WEG", ticker = "WEGE3")
   
    print(empresa_de_motor.name_emp)
    print(empresa_de_motor.ticker_emp)






        





























