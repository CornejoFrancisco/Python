from soporte import*

def principal():

    op = genero_mayor = 0
    opcion_1 = opcion_3 = False
    libros = []

    while op != 8:

        op = menu()

        if op == 1:

            x = int(input('Opte por una carga (1.Manual - 2.Automatica): '))
            while not x in (1,2):
                x = int(input('Opte por una carga (1.Manual - 2.Automatica): '))

            n = validacion(0)

            if x == 1:
                libros += carga_manual(n)
            elif x == 2:
                libros += carga_automatica(n)
            else:
                print('Opcion incorrecta, ingrese un dato valido')

            opcion_1 = True

        elif op == 2:

            if opcion_1:
                listar_libros(libros)
            else:
                print('No existen registros que mostrar. Debe cargarlos.')

        elif op == 3:

            if opcion_1:
                genero_mayor = cantidad_generos(libros)
                opcion_3 = True
            else:
                print('No existen registros que mostrar. Debe cargarlos.')

        elif op == 4:

            if opcion_1:
                precio_mayor(libros)
            else:
                print('No existen registros que mostrar. Debe cargarlos.')

        elif op == 5:

            if opcion_1:
                buscar_isbn(libros)
            else:
                print('No existen registros que mostrar. Debe cargarlos.')

        elif op == 6:

            if opcion_1 and opcion_3:
                consulta_gen(libros,genero_mayor)
            else:
                print('No existen registros que mostrar. Debe cargarlos.')

        elif op == 7:

            if opcion_1:
                precio_de_los_libros = busqueda_de_libro(libros)
                print("El precio total de los libros solicitados es ", precio_de_los_libros)
            else:
                print('No existen registros que mostrar. Debe cargarlos.')

        elif op == 8:
            print('Hasta luego.')
        else:
            print('Error, ingrese una opcion valida.')

if __name__ == '__main__':
    principal()
