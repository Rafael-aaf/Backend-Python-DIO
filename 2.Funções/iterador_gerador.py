
# Precisa ter os métodos __iter__ e __next__

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except:
            raise StopIteration
    

for i in MeuIterador(numeros=[1,2,3]):
    print(i)

print("\n")

# Gerador (tipos de iteradores) - É um iterador, usado quando a tarefa é mais simples

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1,2,3]):
    print(i)