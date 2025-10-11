#Hashmap

pessoa = dict(nome="Rafael", idade=22)
pessoa = {"nome":"Rafael", "idade":22}

print(pessoa["nome"])

contatos = {"rafael@gmail.com":{"nome":"Rafael", "telefone":1111},
            "alice@gmail.com":{"nome":"Alice", "telefone":2222}}

for contato in contatos:
    print(contatos[contato]["telefone"])

for chave, valor in contatos.items():
    print(chave, valor)

#Métodos
copia = contatos.copy()
contatos.clear()
print(copia)
pessoa.update(dict.fromkeys(["Alice", "Anna"], 21))
print(pessoa.get("Alice")) #vantagem para pessoa["Alice"], porque não lança excessão
print(pessoa.get("Diego", {})) #Como não existe, retorna {}
print(pessoa.keys())
print(pessoa.pop("Diego", "não existe"))
#pessoa.popitem()
pessoa.setdefault("Diego", 13) #Se não existe adiciona, se existe não faz nada
print(pessoa)
print(pessoa.values())
print(pessoa.keys())

if "Anna" in pessoa:
    print(True)

pessoa.setdefault("oi", 10)
print(pessoa)
del pessoa["oi"]
print(pessoa)