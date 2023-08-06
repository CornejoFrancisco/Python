import random
import pickle
import os.path

from parcial_n_4 import*

def carga_automatica():
    descripcion_del_producto = ("Fragil", "Peligroso", "Normal", "Joyeria", "Muebles", "Ser vivo", "Articulo de cocina", "Comida")
    entrega = ("Alta Córdoba", "Altamira", "Alto Alberdi", "Alto Hermoso", "Alto Palermo", "Alto Verde", "Betania", "California", "	Camino A Villa Posse", "Ituzaingo", "La Carolina", "La calera")
    numero_de_identificacion = random.randint(1, 1000000)
    descripcion = random.choice(descripcion_del_producto)
    monto_del_envio = random.randint(1, 10000)
    provincia_de_destino = random.randint(0, 23)
    tipo_de_articulo_enviado = random.randint(0, 29)
    barrio_de_entrega = random.choice(entrega)
    return Distribucion(numero_de_identificacion, descripcion, monto_del_envio, provincia_de_destino, tipo_de_articulo_enviado, barrio_de_entrega)


def add_in_orden(v, x):
    n = len(v)
    izq = 0
    pos = 0
    der = n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].numero_de_identificacion == x.numero_de_identificacion:
            pos = c
            break
        elif x.numero_de_identificacion > v[c].numero_de_identificacion:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq
    v[pos:pos] = [x]


def carga_del_vector(n):
    v = []
    for i in range(n):
        distribucion = carga_automatica()
        add_in_orden(v, distribucion)
    return v


def muestra_de_la_carga(v):
    n = len(v)
    for i in range(n):
        print(to_string(v[i]))


def busqueda_por_nombre(v):
    nom = int(input("Ingrese el numero que quiere buscar: "))
    for i in range(len(v)):
        if nom == v[i].numero_de_identificacion:
            print("=" * 60)
            print(to_string(v[i]))
            return
    return print("El numero de identificacion no se encontro...")


def creacion_de_archivo_por_parametro(v, nombre_del_archivo):
    total_de_envio = cantidad_de_envio = 0
    archivo = open(nombre_del_archivo, "wb")
    parametro1 = validacion("Ingrese el monto minimo: ")
    parametro2 = validacion("Ingrse el monto maximo: ")
    for envio in v:
        if envio.tipo_de_articulo_enviado in (2, 5) and parametro1 <= envio.monto_del_envio <= parametro2:
            total_de_envio += envio.monto_del_envio
            cantidad_de_envio += 1
            pickle.dump(envio, archivo)
    archivo.close()
    return total_de_envio, cantidad_de_envio


def muestra_del_archivo(nombre_del_archivo, monto_de_envio, envios_realizados):
    archivo = open(nombre_del_archivo, "rb")
    tam = os.path.getsize(nombre_del_archivo)
    while archivo.tell() < tam:
        Distribucion = pickle.load(archivo)
        print("=" * 60)
        print(to_string(Distribucion))
    archivo.close()
    print("=" * 60)
    print("El promedio de costo de envio es de ", monto_de_envio / envios_realizados)

