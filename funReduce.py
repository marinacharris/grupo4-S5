from functools import reduce
lista =[5,8,5,4]
total = reduce(lambda acumulador, elemento: acumulador + elemento, lista)
total2 = sum(lista)
print(total, total2)