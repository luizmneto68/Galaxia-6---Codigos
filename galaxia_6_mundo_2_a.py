class Empresa:
    def __init__(self, nome_emp, ticker, ano_fundacao, CNPJ): # constructor
        self.nome_emp = nome_emp # atributo
        self.ticker = ticker
        self.ano_fundacao = ano_fundacao
        self.CNPJ = CNPJ

# emp_b3 = Empresa(nome_emp='WEG', ticker='WEGE3')

# print(emp_b3.nome_emp) # WEG

if __name__ == '__main__':
    print('Executando galaxia_6_mundo_2_a.py')