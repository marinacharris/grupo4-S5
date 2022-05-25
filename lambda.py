# función lambda o función anónima
# debe tener una sola instrucción
# sintaxis: lambda argumentos: cuerpo de la función
cuadrado = lambda x: x**2
print(cuadrado(5))

suma = lambda *args: sum(args)

print(suma(4,5,8,6,1))
print(suma(1,8))