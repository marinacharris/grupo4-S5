from math import pow
#sintaxis: map(funcion, objeto iterable)
lista=[1,5,3,7,2,9]
# programación imperativa
lista2 = []
for i in lista:
    lista2.append(i**2)
print(lista2)

#programación funcional
def cuadrado(numero):
    return numero**2
lista3 = list(map(cuadrado, lista))
print(lista3)

# programación funcional con lambda
lista4 = list(map(lambda num: num**2, lista))
print(lista4)

# utilicemos pow de la libreria math

bases = [2,3,5,8,7]
potencias = [0,1,3,2,4]
#A = pow(2,3)
#print(A)
lista5 = list(map(pow,bases,potencias))
print(lista5)
