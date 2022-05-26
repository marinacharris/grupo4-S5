from math import pow
from functools import reduce
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
lista2 = list(map(cuadrado, lista))
print(lista2)

# programación funcional con lambda
lista2 = list(map(lambda num: num**2, lista))
print(lista2)

# utilicemos pow de la libreria math

bases = [2,3,5,8,7]
potencias = [0,1,3,2,4]
#A = pow(2,3)
#print(A)
lista2 = list(map(pow,bases,potencias))
print(lista2)

lista = [
    [1525, [4, 2500],[3,8500],[5,12600]], #[No. factura, [cantidad. precio unidad]...]
    [1520, [3, 2500],[8,12600]],
    [1622, [1, 2500],[5,8500],[2,12600]]    
]
print(lista[0][1][0])

#Generar una lista de listas de la forma [[No.factura, total factura]...[]]
#[No.factura, total1, total2,.... totaln]
listaTotal = list(map(lambda x: [x[0]] + list(map(lambda y: y[0]*y[1],x[1:])),lista))
print(listaTotal)
listaTotal = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a+b,x[1:])],listaTotal))
print(listaTotal)
