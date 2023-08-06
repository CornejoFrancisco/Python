import pickle
import os


def validacion(mensaje):
    num = int(input(mensaje))
    while num < 0:
        num = int(input("ingrese un numero positivo: "))
    return num


# Función para la muestra por pantalla del arreglo ...
def to_string(v):
    cadena = "| {:^35} | {:^15} | {:^15} | {:^15} | {:^15} \n"
    cadena += "{}\n".format("-" * 75)
    return cadena.format(v.identificacion, v.nombre_del_medicamento, v.tipo_de_medicamento, v.modo_de_almacenamiento, v.costo_de_fabricacion)


def punto_2(vector):
    costo_total = 0
    for i in range(len(vector)):
        costo_total += vector[i].costo_de_fabricacion
    promedio_de_costo = (costo_total * 100) / len(vector)

    for j in range(len(vector)):
        if vector[j].costo_de_fabricacion < promedio_de_costo:
            print(to_string(vector[j]))


def create_matriz(v):
    tipo = 10
    modo = 40
    n = len(v)
    matriz = [[0] * modo for i in range(tipo)]

    for i in range(n):
        c = v[i].tipo_de_medicamento
        f = v[i].modo_de_almacenamiento
        matriz[f][c - 1] += 1
    return matriz


def muestra_de_matriz(matriz):
    parametro_de_tipo = int(input("Ingrese el numero del tipo de medicamento: "))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j == parametro_de_tipo:
                print("Tipo de medicamento:", j, "| Modo de almacenamiento:", i, "| Total de medicamento: ", matriz[i][j])


def punto_3(vector):
    matriz = create_matriz(vector)
    muestra_de_matriz(matriz)


def punto_4(v, nombre):
    file = open(nombre, "wb")
    for medicamento in v:
        if medicamento.modo_de_almacenamiento in (2, 5, 9):
            pickle.dump(medicamento, file)
    file.close()
    print("Archivo creado...")
    return nombre


def punto_5(name):
    if not os.path.exists(name):
        print("No existe un archivo llamado {}".format(name))
        return

    acumulador = 0
    tipo_de_medicamento = int(input("Ingrese el numero del tipo de medicamento: "))
    file = open(name, 'rb')
    size = os.path.getsize(name)
    while file.tell() < size:
        medicamento = pickle.load(file)
        if tipo_de_medicamento == medicamento.tipo_de_medicamento:
            acumulador += 1
        print(to_string(medicamento))
    print("El total de registro de ", tipo_de_medicamento, " es de ", acumulador)
    file.close()


def es_vocal(letra):
    vocales = "a", "e", "i", "o", "u"
    return letra in vocales


# Declaración de función que comprueba si la letra es un dígito ...
def es_digito(letra):
    return "1" <= letra <= "9"

def punto_6():
    contador_de_palabras_con_parametro = caracter = 0
    vocal = digito = False
    cadena_de_texto = input("Ingrese el texto que quiere analizar: ").lower()
    for car in cadena_de_texto:
        if car == " " or car == ".":
            if vocal and digito:
                contador_de_palabras_con_parametro += 1
            vocal = digito = False
            caracter = 0
        else:
            caracter += 1
            if es_vocal(car) and caracter == 1:
                vocal = True
            if es_digito(car):
                digito = True
    return contador_de_palabras_con_parametro
