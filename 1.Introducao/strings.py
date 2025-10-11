
nome = "Rafael"

print(nome.upper())
print(nome.lower())
print(nome.title())

nome2 = "   Rafael "

print(nome2.strip())
print(nome2.lstrip())
print(nome2.rstrip())
print(nome.center(9, "#"))
print(".".join(nome))

PI = 3.1415926

print(f'Valor de pi: {PI:.4f}')
print(f'Valor de pi: {PI:10.4f}')

#nome[start:stop:step]
print(nome[:2])
print(nome[2:])
print(nome[0:5:2])
print(nome[::-1])

#Strings multiplas linhas ou Strings triplas

mensagem = f"""
Olá meu nome é {nome},
Oiiiiii.
"""

print(mensagem)