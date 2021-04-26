nombre = input('Digame su nombre: ')

apellido = input('Digame su apellido: ')

edad = int(input('Digame su edad: '))

condicion = ''

if edad <0:
    condicion = 'nonato'
elif edad <18:
    condicion = 'menor'
elif edad <65:
    condicion = 'mayor'
elif edad <120:
    condicion = 'jubilado'
else:
    condicion = 'cadaver'

frase = 'Su nombre es: ' + nombre + ' ' + apellido + ' y usted es ' + condicion
print(frase)
frase2 = ('Su nombre es {} {} y usted es {}'.format(nombre,apellido,condicion))
print(frase2)
