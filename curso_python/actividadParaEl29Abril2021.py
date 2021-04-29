def rangoEdad(edad):
    if edad <18:
        return 'menor'
    elif edad <65:
        return 'mayor'
    elif edad <=120:
        return 'jubilado'

def catalogoPorEdad(condicion):
    if condicion == 'menor':
        return catalogoParaMenor()
    elif condicion == 'mayor':
        return catalogoParaMayor()
    else:
        return catalogoParaJubilado()

def catalogoParaMenor():
    esElectronico = input('Busca en la seccion de electronicos? (responda con si o no)')
    while esElectronico != 'si' and esElectronico != 'no':
        esElectronico = input('Busca en la seccion de juguetes electronicos? (responda con si/no)')
    colorJuguete = input('En que color esta buscando: ')
    puedeCaminar = input('Busca un juguete que pueda caminar/articulable? (responda con si o no)')
    while puedeCaminar != 'si' and puedeCaminar != 'no':
        puedeCaminar = input('Busca un juguete que pueda caminar o sea articulable? (responda con si/no)')
    return "juguete electronico = {}, de color {} y que pueda caminar = {}".format(esElectronico,colorJuguete,puedeCaminar)

def catalogoParaMayor():
    tipoRopa = input('Busca camisa o pantalon?')
    while tipoRopa != 'camisa' and tipoRopa != 'pantalon':
        tipoRopa = input('Busca camisa o pantalon? (responda con camisa/pantalon)')
    colorRopa = input('En que color esta buscando: ')
    talleRopa = input('En talle esta buscando: ')
    return "{} de color {} y del talle {}".format(tipoRopa,colorRopa,talleRopa)

def catalogoParaJubilado():
    pasajeA = input('Busca viajar a Federacion, Cataratas o Santa Teresita?')
    while pasajeA != 'Federacion' and pasajeA != 'Cataratas' and pasajeA != 'Santa Teresita':
        pasajeA = input('Busca viajar a Federacion, Cataratas o Santa Teresita? (responda con una de las opciones)')
    return "pasaje a {}".format(pasajeA)


cantidad_personas = int(input('Ingrese cuantas personas:'))

for i in range(0, cantidad_personas):
    nombre = input('Digame su nombre: ')
    apellido = input('Digame su apellido: ')
    edad = int(input('Digame su edad (entre 1 a 120 años)'))
    while edad < 1 or edad > 120:
        edad = int(input('Digame su edad (entre 1 a 120 años)'))

    condicion = rangoEdad(edad)
    fraseProductoSelcionado = catalogoPorEdad(condicion)

    frase = ('Su nombre es {} {} y usted es {} y el producto selecionado es: \n{}'.format(nombre,apellido,condicion,fraseProductoSelcionado))
    print(frase)
