import funciones

while True:

    funciones.crear_tabla()

    print("ingrese la opcion que desea ejecutar ")
    print("Opción 1: Insertar un registro de empleado")
    print("Opción 2: Seleccionar un registro de empleado a partir de su número de DNI")
    print("Opción 3: Seleccionar todos los empleados o los registros de la tabla")
    print("Opción 4: Modificar el área de un empleado en función de su número de legajo")
    print("Opción 5: Eliminar un empleado a partir de su número de legajo")
    print("Opción 6: Finalizar")
    opcion = input("ingrese la opcion: ")
    if opcion == "1":
        while True:
            valores = []
            valor1 = int(input("ingrese el numero de legajo "))
            valores.append(valor1)
            valor2 = int(input("ingrese el dni: "))
            valores.append(valor2)
            valor3 = input("ingrese el nombre: ")
            valores.append(valor3)
            valor4 = input("ingrese el apellido: ")
            valores.append(valor4)
            valor5 = input("ingrese el area en la que trabaja: ")
            valores.append(valor5)
            funciones.insertar_nuevo_registro(valores)
            break

    elif opcion == "2":
        try:

            while True:
                try:
                    funciones.seleccionar_unregistro(input("ingrese un dni: "))
                    break
                except ValueError:
                    print("el dni debe ser numerico")
        except ValueError:
            print("ingrese un dni correcto")

    elif opcion == "3":

        funciones.seleccionar_todos_registros()

    elif opcion == "4":

        while True:
            try:
                numero_legajo = int(input("ingrese el numero de legajo: "))
                area = input("ingrese la nueva area: ")
                funciones.modificar_registros(numero_legajo, area)

                break
            except ValueError:
                print("el legajo debe ser numerico")

    elif opcion == "5":

        while True:
            try:
                numero_legajo = int(input("ingrese el numero de legajo: "))

                break

            except ValueError:
                print("ingrese un valor entero")

        funciones.eliminar_registros(numero_legajo)

    else:
        break
