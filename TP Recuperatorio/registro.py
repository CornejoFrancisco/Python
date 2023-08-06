# Se solicita un pequeño sistema para administrar listas de música personalizadas.
# Su primera tarea es crear, mediante un módulo separado, un archivo de texto “musica.csv”
# con los datos de los temas musicales generados en forma aleatoria. Por cada tema en el archivo
# de texto, debe haber una línea con los datos siguientes:
#
# Título o nombre.
# Género: 0-Balada, 1-Pop, 2-Rock, 3-Folclore, 4-Electrónica, 5-Otros.
# Idioma Original: 0-Español, 1: Inglés, 2: Francés, 3: Portugués, 4:Otros.
# Su segunda tarea es desarrollar un programa que incluya la definición del tipo registro Tema
# (con un campo por cada dato contenido en el archivo de texto para un tema), y tal que el
# programa esté controlado por menú de opciones que permita:

# Importe de librerias ...
import os
import pickle
from carga_de_los_temas import*


# Función para la creación del archivo ...
def creacion_del_archivo(v, nombre_del_archivo):
    file = open(nombre_del_archivo, "wb")
    for tema in v:
        pickle.dump(tema, file)
    file.close()


# Función para el ordenado del vector ...
def order(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i + 1, n):
            if v[i].titulo > v[j].titulo:
                v[i], v[j] = v[j], v[i]


# Función para la carga de los datos del vector al archivo ...
def archivo(vector):
    order(vector)
    creacion_del_archivo(vector, NOMBRE_ARCHIVO)


# Función para la validación de números mayor a 0 ...
def validar(mensaje):
    n = int(input(mensaje))
    while n < 0:
        n = int(input("Ingrese número positivo: "))
    return n


# Validación de rango ...
def validar_entre(mensaje, menor, mayor):
    n = int(input(mensaje))
    while mayor <= n <= menor:
        n = int(input("Ingrese un número: "))
    return n


# Función para la muestra de archivo por pantalla ...
def muestra_del_archivo(nombre_del_archivo):
    file = open(nombre_del_archivo, "rb")
    size = os.path.getsize(nombre_del_archivo)
    print(encabezado())
    while file.tell() < size:
        tema = pickle.load(file)
        print(to_string(tema))

    file.close()


# Función de soporte de generar_vector_temas_idiomas ...
def vector_de_libros_selecionado(vector, temas_solicitados, idioma_solicitado):
    n = len(vector)
    contador = 0
    vector_de_temas = []
    for i in range(n):
        if contador != temas_solicitados:
            if vector[i].idioma == idioma_solicitado:
                contador += 1
                vector_de_temas.append(vector[i])

    return vector_de_temas


# Función para la creación de vector con la cantidad de canciones e idioma solicitado ...
def generar_vector_temas_idiomas(vector):
    cantidad_temas_solicitado = validar("Ingrese la cantidad de temas: ")
    idioma_solicitado = validar_entre("Ingrese número de idioma (0-Español, 1: Inglés, "
                                      "2: Francés, 3: Portugués, 4:Otros.): ", 0, 4)
    canciones_con_parametros = vector_de_libros_selecionado(vector, cantidad_temas_solicitado,
                                                            idioma_solicitado)

    if len(canciones_con_parametros) < cantidad_temas_solicitado:
        print("=" * 60)
        print("- No hay suficiente canciones con ese idioma...")
        print(encabezado())
        for i in range(len(canciones_con_parametros)):
            print(to_string(canciones_con_parametros[i]))
        print("=" * 60)
    else:
        print(encabezado())
        for i in range(len(canciones_con_parametros)):
            print(to_string(canciones_con_parametros[i]))


# Función para crear matriz de conteo ...
def create_matriz(v):
    idiomas = 5
    generos = 6
    n = len(v)
    matriz = [[0] * idiomas for i in range(generos)]

    for i in range(n):
        c = v[i].idioma
        f = v[i].genero
        matriz[f][c] += 1
    return matriz


# Función para la muesta de matriz por pantalla ...
def muestra_de_la_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > 0:
                print("- Tipo de género: ", i, "| Idioma: ", j, "| La cantidad es de: ", matriz[i][j])


# Función para la creación y muestra por pantalla de matriz ...
def generar_matriz(v):
    matriz = create_matriz(v)
    muestra_de_la_matriz(matriz)
    return matriz


# Función para contar dentro de la matriz ...
def conteo_de_matriz(matriz, genero):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if genero == i:
                suma += matriz[i][j]
    return suma


# Función para  determinar la cantidad de temas musicales para el género seleccionado ...
def contar_temas_genero(matriz):
    print('(Género: 0-Balada, 1-Pop, 2-Rock, 3-Folclore, 4-Electrónica, 5-Otros)')
    genero_para_conteo = validar_entre("Ingrese el número del genero que quiere realizar el conteo: ", 0, 5)
    suma = conteo_de_matriz(matriz, genero_para_conteo)
    print("La cantidad de temas sobre el género", genero_para_conteo, "es de ", suma)


# Función de respaldo para la búsqueda de tema ....
def busqueda_del_tema(v, x):
    izq, der = 0, len(v)-1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c].titulo:
            return c
        if x < v[c].titulo:
            der = c - 1
        else:
            izq = c + 1
    return -1


# Función para la muestra de tema buscado ...
def muestra_de_la_cancion_entontrada(v, posicion_cancion):
    if posicion_cancion != -1:
        print(encabezado())
        print(to_string(v[posicion_cancion]))
    else:
        print("No se encontró esa canción...")


# Función para realizar búsqueda por título del tema
def buscar_tema_titulo(vector):
    titulo_buscado = str(input("Ingrese el título de la canción que busca: ")).upper()
    informacion_de_la_cancion = busqueda_del_tema(vector, titulo_buscado)
    muestra_de_la_cancion_entontrada(vector, informacion_de_la_cancion)


# Función de respaldo para crear archivo binario ...
def creacion_del_archivo_con_parametros(v, idioma):
    nombre = 'MusicaIdioma' + str(idioma) + '.dat'
    file = open(nombre, "wb")
    for tema in v:
        if tema.idioma == idioma:
            pickle.dump(tema, file)
    file.close()
    return nombre


# Función para generar archivo binario con genero seleccionado ...
def generar_archivo_binario(vector):
    idioma_elegido = validar_entre("Idiomas -> 0: Español, 1: Inglés, 2: Francés, 3: Portugués, 4: Otros"
                                   "\n- Ingrese número de idioma: ", 0, 4)
    nombre = creacion_del_archivo_con_parametros(vector, idioma_elegido)

    print('... ¡Hecho! ヾ(≧▽≦*)o')
    return nombre


# Función para la muestra por pantalla del encabezado del arreglo ...
def encabezado():
    cadena = '{}\n'.format('-' * 75)
    cadena += '| {:^35} | {:^15} | {:^15} |\n'
    cadena += '{}\n'.format('-' * 75)
    return cadena.format('Título', 'Género', 'Idioma')


# Función para la muestra por pantalla del arreglo ...
def to_string(v):
    cadena = '| {:^35} | {:^15} | {:^15} |\n'
    cadena += '{}\n'.format('-' * 75)
    return cadena.format(v.titulo, v.genero, v.idioma)
