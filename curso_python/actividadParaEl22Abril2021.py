cantidad_personas = int(input('Ingrese cuantas personas:'))

for i in range(0, cantidad_personas):
    nombre = input('Digame su nombre: ')
    apellido = input('Digame su apellido: ')
    edad = int(input('Digame su edad (debe estar entre 1 a 120 años)'))
    while edad < 1 or edad > 120:
        edad = int(input('Digame su edad (debe estar entre 1 a 120 años)'))

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

    frase = ('Su nombre es {} {} y usted es {}'.format(nombre,apellido,condicion))
    print(frase)
