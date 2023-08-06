# Turno 1 - Enunciado 2 (T1E2) (Copie el enunciado siguiente como comentario al inicio de su archivo principal de código fuente)
#
# Una empresa que distribuye artículos a diferentes puntos del país necesita mantener información sobre los distintos
# envíos que realiza. Por cada envío se registran los siguientes datos: número de identificación (un entero), descripción
# del envío (una cadena), monto del envío, provincia destino (un valor entre 0 y 23 incluidos, por ejemplo: 0: Córdoba
# , 1: San Luis, etc.), tipo de artículo enviado (un número entero entre 0 y 29 incluidos, para indicar (por ejemplo): 0:
# silla, 1: computadora, etc.) y el barrio de entrega (una cadena). Se pide definir un tipo registro Envio con los campos
# que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:
#
# 1- Cargar los datos de n registros de tipo Envío en un arreglo de registros (cargue n por teclado). El arreglo debe
# crearse de forma que siempre quede ordenado de menor a mayor, según el número de identificación de los envíos, y para
# hacer esto debe aplicar el algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta
# la solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada
# pero con búsqueda secuencial. Puede cargar los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga
# manual, TODA la carga debe ser manual, y si la hace automática entonces TODA debe ser automática). Valide que la
# provincia destino y el tipo de artículo estén dentro de los valores descriptos y recuerde que estos son números enteros.
#
# 2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea, pero muestre solo los datos de los registros
# cuyo tipo sea mayor al valor k que se carga por teclado.
#
# 3- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación sea igual a num (cargar
# num por teclado). Si existe, mostrar por pantalla todos sus datos. Si no existe, informar con un mensaje. La búsqueda
# debe detenerse al encontrar el primer registro que coincida con el patrón pedido.
#
# 4- Guarde en un archivo los registros del arreglo cuyo tipo de articulo vendido sea 2 o 5 y cuyo monto del envío este
# comprendido entre dos valores x e y (ambos incluidos) que se ingresan por teclado.
#
# 5- Muestre el archivo que creó en el punto 4, a razón de un registro por línea en la pantalla y al final mostrar una
# línea adicional que informe el promedio de los montos de los envíos que se mostraron.

from servicios import*

Nombre_del_archivo = "Rutadeenvios.dat"

class Distribucion:
    def __init__(self, numero_de_identificacion, descripcion, monto_del_envio, provincia_de_destino, tipo_de_articulo_enviado, barrio_de_entrega):
        self.numero_de_identificacion = numero_de_identificacion
        self.descripcion = descripcion
        self.monto_del_envio = monto_del_envio
        self.provincia_de_destino = provincia_de_destino
        self.tipo_de_articulo_enviado = tipo_de_articulo_enviado
        self.barrio_de_entrega = barrio_de_entrega


def to_string(distribucion):
    template = "Numero de identificacion: {} | Descripcion: {} | Monto de envio: {} | Provincia de destino: {} | Tipo de articulo enviado: {} |Barrio de entrega: {}"
    return template.format(distribucion.numero_de_identificacion, distribucion.descripcion, distribucion.monto_del_envio,
                           distribucion.provincia_de_destino, distribucion.tipo_de_articulo_enviado, distribucion.barrio_de_entrega)


def menu():
    print("1 - Creacion del arreglo.")
    print("2 - Muestra del arreglo.")
    print("3 - Busqueda por numero de identificacion.")
    print("4 - Creacion del archivo.")
    print("5 - Muestra del archivo creado en el punto 4")
    print("6 - Se cierra el programa.")


def validacion(mensaje):
    n = int(input(mensaje))
    while 0 > n:
        n = int(input("Ingrese un numero positvo: "))
    return n

def principal():
    op = -1
    cargado = creado_el_archivo = False
    while op != 6:
        print("=" * 60)
        menu()
        print("=" * 60)
        op = validacion("Ingrese el numero del programa: ")
        if op == 1:
            cargado = True
            n = validacion("Ingrese la cantidad de envios realizados: ")
            v = carga_del_vector(n)
        elif op == 2:
            if cargado:
                muestra_de_la_carga(v)
        elif op == 3:
            if cargado:
                busqueda_por_nombre(v)
        elif op == 4:
            if cargado:
                creado_el_archivo = True
                costo_de_envios, cantidad_de_envios = creacion_de_archivo_por_parametro(v, Nombre_del_archivo)
        elif op == 5:
            if cargado:
                if creado_el_archivo:
                    muestra_del_archivo(Nombre_del_archivo, costo_de_envios, cantidad_de_envios)
                else:
                    print("Todavia no se creo el archivo.")
        elif op == 6:
            print("Se cierra el programa.")

if __name__ == '__main__':
    principal()
