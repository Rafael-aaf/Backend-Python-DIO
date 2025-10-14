
# Função dentro de uma função
def calcular(operacao):
    def somar(a, b):
        return a + b
    def subtrair(a, b):
        return a - b
    if operacao == "+":
        return somar
    else:
        return subtrair

print(calcular("+")(1,2))
print(calcular("-")(1,2))

print("\n")

# Decorator:
def meu_decorator(func):
    def wrapper():
        print("Faz algo antes da função")
        func()
        print("Faz algo depois da função")

    return wrapper

@meu_decorator
def oi():
    print("Oiii")

# sem o @meu_decorator antes da função:
# oi = meu_decorator(oi)
# oi()
oi()

print("\n")

# Decorators com argumentos

import math

def valida_positivo(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError("Todos os argumentos devem ser positivos")
        for arg in kwargs.values():
            if arg < 0:
                raise ValueError("Todos os argumentos devem ser positivos")
        return func(*args, **kwargs)
    return wrapper


@valida_positivo
def raiz_quadrada(x):
    return math.sqrt(x)


@valida_positivo
def divisao(a, b):
    return a / b


if __name__ == "__main__":
    print(raiz_quadrada(36))  
    print(divisao(12, 3))  

    try:
        print(raiz_quadrada(-25))
    except ValueError as e:
        print(f"Erro: {e}")

    try:
        print(divisao(8, -2))
    except ValueError as e:
        print(f"Erro: {e}")


# functools: Mantêm nome e parâmetros da função. Tem relação com Introspecção
# functools.wraps(func)