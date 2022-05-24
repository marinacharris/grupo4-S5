def suma(*args):
    #total = 0
    #for i in args:
    #    total += i #total = total + i
    return sum(args)

print(suma(4,5))
print(suma(4,8,5,9,7,9))
print(suma(8,1,2))

def suma(**kwargs):
    return sum(kwargs.values())

print(suma(a=4,b=6,c=7))