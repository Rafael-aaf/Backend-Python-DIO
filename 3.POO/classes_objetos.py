# Classe: Define as caracteristicas e comportamentos de um objeto.
# Porém não pode ser usada diretamente.

# Objetos: Podem ser usados (sua instância).
# Posuem caracterpisticas e comportamentos que foram definaidos nas classes

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("auauauauauuaau")

    def dormir(self):
        self.acordado = False
        print("Zzzzz.....")
    
Dory = Cachorro("Dory", "Preta e Branca")
Dory.latir()
Dory.dormir()

Chico = Cachorro("Chico", "Preto e Branco", False)
Chico.latir()
Chico.dormir()