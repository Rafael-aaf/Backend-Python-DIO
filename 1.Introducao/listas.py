
ls = ["Rafael", 22, True]
numeros = list(range(10))
ls_ls = [[1,2,3],[4,5,6],[7,8,9]]

print(ls)
print(numeros)
print(ls_ls)

for numero in numeros:
    print(numero)

for i, numero in enumerate(numeros):
    print(f'{i}, {numero}')

# List Comprehension
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

#Métodos
lista = [10,20,30,30]
lista.append(40)
lista2 = lista.copy()
lista.clear()
lista = [50,60,70]
lista.extend(lista2)

print(lista)
print(lista2)
print(lista2.count(30))
print(lista.index(20))

lista.pop() # Funciona como Pilha também
print(lista)

lista.remove(10)
lista.reverse()
print(lista)

lista.sort(reverse=False, key=lambda x: len(lista))
print(lista)

sorted(lista, key=lambda x: len(lista), reverse=False)