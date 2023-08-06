import random

# Registros aleatorios
codigos_random = ['85-608-7388-0','601-121-781-8','601-934-625-0','84-8181-227-7','11-111-11-111',
                  '601-121-781-8','85-608-7388-0','601-934-625-0']
titulos_random = ['Las aventuras de Nala', 'Cartas del pasado', 'Misterios del futuro', 'Messi en el PSG',
                  'Milanesa con puré', 'Calculo diferencial', 'Hamburguesas de verdad']

def print_genero():
    print('\n0 - Autoayuda', '\n1 - Arte', '\n2 - Ficción', '\n3 - Computación', '\n4 - Economía',
          '\n5 - Escolar', '\n6 - Sociedad', '\n7 - Gastronomía', '\n8 - Infantil', '\n9 - Otros')

def print_idioma():
    print('\n0 - Español', '\n1 - Inglés', '\n2 - Francés', '\n3 - Italiano', '\n4 - Otros')

class Libro:
    def __init__(self, codigo, titulo, genero, idioma, precio):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.precio = precio

def muestra(libro):
    print("ISBN: ", libro.codigo,end=' ')
    print("Titulo: ", libro.titulo,end=' ')
    print("Genero: ", genero_idioma(libro.genero,-100),end=' ')
    print("Idioma: ", genero_idioma(-100, libro.idioma),end=' ')
    print("Precio: ", libro.precio,end=' ')

def write(libro):
    linea = "{:<15}\t{:<30}\t{:>15}\t{:>15}\t{:>8}"
    return linea.format(libro.codigo, libro.titulo, libro.genero, libro.idioma, libro.precio)

# Menú
def menu():
    print('=' * 60)
    print('1. Generacion y carga')
    print('2. Mostrar todos los libros')
    print('3. Stock y genero mas popular')
    print('4. Busqueda del mayor')
    print('5. Busqueda por ISBN y aumento')
    print('6. Consulta de un genero')
    print('7. Consulta de precio por grupo')
    print('8. Salir')
    print('=' * 60)

    op = int(input('Ingrese una opcion: '))
    print('=' * 60)
    return op

def carga_manual(n):
    v = []

    for i in range(n):
        codigo = input('Ingrese el codigo: ')
        while not validar_isbn(codigo):
            codigo = input('Ingrese un codigo valido: ')
        titulo = input('Ingrese el titulo: ')
        print_genero()
        genero = int(input('Ingrese el genero: '))
        while not genero in (1,2,3,4,5,6,7,8,9,10):
            genero = int(input('Ingrese el genero: '))
        print_idioma()
        idioma = int(input('Ingrese el idioma: '))
        while not idioma in (1,2,3,4,5):
            idioma = int(input('Ingrese el idioma: '))
        precio = float(input('Ingrese el precio: '))
        libro = Libro(codigo, titulo, genero, idioma, precio)
        v.append(libro)

    return v

def carga_automatica(n):
    v = []

    for i in range(n):
        codigo = random.choice(codigos_random)
        titulo = random.choice(titulos_random)
        genero = random.randint(0,9)
        idioma = random.randint(0,4)
        precio = float(random.randint(0,5000))
        libro = Libro(codigo, titulo, genero, idioma, precio)
        v.append(libro)

    return v

# Muestra todos los libros
def listar_libros(v):
    m = 0
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].titulo < v[j].titulo:
                v[i], v[j] = v[j], v[i]

    for i in range(n):
        if v[m].genero in (0,1,2,3,4,5,6,7,8,9):
            v[m].genero = genero_idioma(v[m].genero,-100)
            v[m].idioma = genero_idioma(-100, v[m].idioma)
        m += 1

    print('---Codigo--- / -- Titulo -- / Genero / Idioma / Precio')
    for libro in v:
        print(write(libro))

def validacion(num):
    n = num
    while n <= num:
        n = int(input("Ingrese el numero de libros: "))
        if n <= num:
            print(int(input("Error: no puede ingresar un valor negativo. Intente nuevamente")))
    return n

def validar_isbn(v):

    m = 10
    suma = guion = 0
    carant = ''
    guion_seguido = False

    if len(v) != 13 or v[0] == '-':
        return False

    for car in v:

        if car == '-':
            guion += 1
            if carant == '-':
                guion_seguido = True
        else:
            suma += int(car) * m
            m -= 1

        carant = car

    if guion_seguido:
        return False

    if (suma % 11) == 0 and guion == 3:
        return True
    else:
        return False

def genero_idioma(num_genero, num_idioma):

    generos = ('Autoayuda', 'Arte', 'Ficcion', 'Computacion', 'Economia', 'Escolar',
               'Sociedad', 'Gastronomia', 'Infantil', 'Otros')
    idiomas = ('Espanol', 'Ingles', 'Frances', 'Italiano', 'Otros')

    if num_genero != -100:
        if num_genero >= 0 <= len(generos):
            return generos[num_genero]
        else:
            return "N/A"

    if num_idioma != -100:
        if num_idioma >= 0 <= len(idiomas):
            return idiomas[num_idioma]
        else:
            return "N/A"

def busqueda_de_mayor(c):
    n = len(c)
    for i in range(n-1):
        for j in range(i+1, n):
            if c[j] > c[i]:
                c[j], c[i] = c[i], c[j]

    return c[0]

# Punto 3
def cantidad_generos(vec):

    v = inversa_str(vec)

    c = [0] * 10
    mayor = 0
    n = len(v)
    genero_mayor = 0

    for i in range(n):
        gen = v[i].genero
        c[gen] += 1

    print('Cantidad de libros por genero:')
    for r in range(10):
        if c[r] != 0:
            print('Genero: ', genero_idioma(r,-100), 'Cantidad de apariciones:', c[r])
        if c[r] > mayor:
            genero_mayor = r
            mayor = c[r]

    print('El genero de mayor cantidad es: ', genero_idioma(genero_mayor, -100))

    return genero_mayor

# Punto 4
def precio_mayor(vec):

    v = inversa_str(vec)
    n = len(v)
    mayor = 0
    libro_mayor = None

    print_idioma()
    i = int(input('Ingrese el idioma: '))
    while not i in (0,1,2,3,4):
        i = int(input('Ingrese el idioma: '))

    for c in range(n):
        if v[c].idioma == i:
            if v[c].precio > mayor:
                mayor = v[c].precio
                libro_mayor = v[c]

    if libro_mayor is None:
        print('No hay libros de ese idioma')
    else:
        print("El libro de mayor precio es: ")
        muestra(libro_mayor)
        print('\n')

# Punto 5
def buscar_isbn(v):
    codigo = input('ingrese codigo que desea buscar:')
    existe = False

    for i in range(len(v)):
        if v[i].codigo == codigo:
            existe = True
            muestra(v[i])
            aumento = v[i].precio / 100 * 10
            precio = v[i].precio + aumento
            print("precio actualizado ", str(precio))

    if not existe:
        print("No existe ningun libro con ese codigo")

def busqueda_de_libro(v):
    precio = 0
    cantidad = int(input("Ingrese la cantidad de libros que quiere buscar: "))
    m = len(v)
    c = 0
    vec = []

    for i in range(cantidad):

        libro_de_busqueda = input("Codigo de libro a buscar: ")
        while not validar_isbn(libro_de_busqueda):
            libro_de_busqueda = input('Ingrese un codigo valido: ')

        for j in range(m):
            if v[j].codigo == libro_de_busqueda:
                c += 1
                precio += v[j].precio

                vec.append(v[j])

        if c > 1:
            print("Hay", c,"concidencia/s con el codigo ISBN.")
            for p in range(len(vec)):
                muestra(vec[p])
                print('\n')
        else:
            print('No se encontraron libros con el ISBN ingresado')

    return precio

def consulta_gen(v, genero_mayor):

    n = len(v)
    print(genero_mayor)

    for g in range(n):
        if v[g].genero == genero_mayor:
            for i in range(n-1):
                for j in range(i+1, n):
                    if v[i].precio > v[j].precio:
                        v[i], v[j] = v[j], v[i]

    for libro in v:
        if libro.genero == genero_mayor:
            print(muestra(libro))

# Fue la unica solución que encontramos tras 5h buscando el error.
# Saludos :^)
def inversa_str(v):

    for i in range(len(v)):
        if v[i].genero == 'Autoayuda':
            v[i].genero = 0
        if v[i].genero == 'Arte':
            v[i].genero = 1
        if v[i].genero == 'Ficcion':
            v[i].genero = 2
        if v[i].genero == 'Computacion':
            v[i].genero = 3
        if v[i].genero == 'Economia':
            v[i].genero = 4
        if v[i].genero == 'Escolar':
            v[i].genero = 5
        if v[i].genero == 'Sociedad':
            v[i].genero = 6
        if v[i].genero == 'Gastronomia':
            v[i].genero = 7
        if v[i].genero == 'Infantil':
            v[i].genero = 8
        if v[i].genero == 'Otros':
            v[i].genero = 9

        if v[i].idioma == 'Espanol':
            v[i].idioma = 0
        if v[i].idioma == 'Ingles':
            v[i].idioma = 1
        if v[i].idioma == 'Frances':
            v[i].idioma = 2
        if v[i].idioma == 'Italiano':
            v[i].idioma = 3
        if v[i].idioma == 'Otros':
            v[i].idioma = 4

    return v
