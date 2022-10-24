import sqlite3


def conection_db():
    bd = sqlite3.connect("Empleados.db")
    return bd


def crear_tabla(cursor):

    cursor.execute('''CREATE TABLE  IF NOT  EXISTS empleados (
	"id"	INTEGER NOT NULL,
	"numero_legajo"	INTEGER NOT NULL UNIQUE,
    "dni"	INTEGER NOT NULL UNIQUE,
	"nombre_empleado"	TEXT NOT NULL,
	"apellido_empleado"	TEXT NOT NULL,
	"area"	TEXT NOT NULL,
	PRIMARY KEY("id"AUTOINCREMENT));''')


def insertar_nuevo_registro(bd, cursor, valores):

    cursor.execute("INSERT INTO empleados VALUES(NULL,?,?,?,?,?)", valores)
    bd.commit()
    bd.close()


def seleccionar_unregistro(cursor, dni):

    cursor.execute('SELECT * FROM empleados WHERE dni=?', [dni])
    print(cursor.fetchone())


def seleccionar_todos_registros(cursor):
    db = conection_db()

    cursor.execute('SELECT * FROM empleados',)
    print(cursor.fetchall())
    bd.commit()
    bd.close()


def modificar_registros(bd, cursor, numero_legajo, area):

    sentencia = "UPDATE empleados SET area = ?  WHERE numero_legajo = ?;"
    cursor.execute(sentencia, [area, numero_legajo])
    bd.commit()
    bd.close()
    print("el area de trabajo del empleado con el legajo {} fue actualizada a{}".format(
        numero_legajo, area))


def eliminar_registros(bd, cursor, numero_legajo):

    sentencia = "DELETE FROM empleados WHERE numero_legajo = ?;"
    cursor.execute(sentencia, [numero_legajo])
    bd.commit()
    bd.close()
    print("Datos eliminados")


while True:
    bd = conection_db()
    cursor = bd.cursor()
    crear_tabla(cursor)

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

            try:

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

                insertar_nuevo_registro(bd, cursor, valores)
                break
            except ValueError:
                print("ingrese los datos del tipo correcto")

    elif opcion == "2":
        try:

            while True:
                try:
                    seleccionar_unregistro(cursor, input("ingrese un dni: "))
                    break
                except ValueError:
                    print("el dni debe ser numerico")
        except ValueError:
            print("ingrese un dni correcto")

    elif opcion == "3":

        seleccionar_todos_registros(cursor)

    elif opcion == "4":

        while True:
            try:
                numero_legajo = int(input("ingrese el numero de legajo: "))
                area = input("ingrese la nueva area: ")
                modificar_registros(bd, cursor, numero_legajo, area)

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

        eliminar_registros(bd, cursor, numero_legajo)

    else:
        break
