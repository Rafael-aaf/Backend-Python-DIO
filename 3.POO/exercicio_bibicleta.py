
class Bibicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print(f'Bibibi')
    
    def parar(self):
        print(f'PARAAA')
    
    def correr(self):
        print(f'Correndo')

    def __str__(self): # Retorna os atributos da classe
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
bibicleta_1 = Bibicleta("azul", "modelo 3", 2016, 200)

bibicleta_1.buzinar()
bibicleta_1.parar()
bibicleta_1.correr()
print(bibicleta_1)

Bibicleta.buzinar(bibicleta_1)