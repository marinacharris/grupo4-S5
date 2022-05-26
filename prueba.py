a = [0,5,2,1]
b = [9,6,5]
c = a + b 
print(c)
print(c[:3])
print(c[4:])
print(c[2:5])

a = 10
if a == 10:
    print('ok')
else:
    print('Error')
    
print('ok') if a == 10 else print('Error')

a = round(452323.667894,2)
print(f'el valor es {a:,.2f}')
