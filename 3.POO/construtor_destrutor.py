
# Método Construtor - Sempre executado quando uma nova
# instância da classe é criada. Inicializa-se o estado do objeto
# __init__ (inicializador/construtor)

# Método Desconstrutor - Sempre é executado quando uma instância
# é destruída. Não é tão necessário, pois em Python há um coletor de lixo.
# __del__

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        #pass - pode ter somente um pass!
        print("Removendo a instância da classe")

    def falar(self):
        print("Auauauauuauauuauuau")

dory = Cachorro("Dory", "Preto e Branco")
dory.falar()

print("Oii")
#del dory - força o programa a destruir a instância dory :(
print("Oii")
print("Oii")
print("Oii")