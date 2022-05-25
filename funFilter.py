# realiza un filtro sobre una coleccion de datos
# la función que ytiliza debe retornar una valor booleano
# sintaxis: filter(función, objeto iterable)
# la función retorna un filter object

lista = [5,8,21,3,44,1,5,98]

pares = list(filter(lambda x: x%2 == 0, lista))
print(pares)

lista2 = ['Marina', 'Carlos','Sofía','Ana', 'Arturo', 'Laura']
nombresA = list(filter(lambda nombre: nombre[0]=='A',lista2))
print(nombresA)

diccionarios={
    'a':1,
    'b':4,
    'c':30,
    'd':20,
    'f':6
}
diccionario2 = dict(filter(lambda x: x[1]>5 , diccionarios.items()))
print(diccionario2)


