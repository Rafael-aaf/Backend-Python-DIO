
def numero(a):
    antecessor = a - 1
    sucessor = a + 1
    return antecessor, sucessor # Retorna uma tupla

print(numero(9))

def imprimir(nome):
    print(f'Olá, {nome}')

print(imprimir("Rafael")) # Retorna None para função sem return

imprimir("Rafael") # Argumento posicional
imprimir(nome="Rafael") # Argumento nomeado
imprimir(**{"nome":"Rafael"}) # Argumento passado como dicionário

# Args (*args), tupla
#Kwargs (**kwargs), dicionário

#Parâmetros Especiais:

def pessoa(*, nome, idade, email, telefone): # Os parâmetros devem ser passados nomeados
    print(nome, idade, email, telefone)

pessoa(nome="Rafael", idade=22, email="rafa@gmail.com", telefone=1111)

def pessoa(nome, idade, email, telefone, /): # Os parâmtetro devem ser passados posicionais
    print(nome, idade, email, telefone)

pessoa("Rafael", 22, "rafa@gmail.com", 1111)

def pessoa(nome, idade, /, *, email, telefone): # Híbrido
    print(nome, idade, email, telefone)

pessoa("Rafael", 22, email="rafa@gmail.com", telefone=1111)

#Função como objeto de primeira classe

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)

op = somar # Atribuindo função a uma variável
print(op(5,6))

# Escopo local e global. Usar a keyword 'global' é mal prática
salario = 1000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario
    
print(salario_bonus(500))