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
	PRIMARY KEY("id"));'''
    )

def insertar_nuevo_registro(cursor,valores):
    conection_db()
    cursor.execute("INSERT INTO empleados VALUES(?,?,?,?,?,?)",valores)
    bd.commit()
    bd.close()

def seleccionar_unregistro(cursor,dni):
   
    cursor.execute('SELECT * FROM empleados WHERE dni=?', [dni])
    print(cursor.fetchone())
  

def seleccionar_todos_registros(cursor):
    
    cursor.execute('SELECT * FROM empleados',)
    print(cursor.fetchall())
   

def modificar_registros(cursor, numero_legajo,area):
    conection_db()
    sentencia = "UPDATE empleados SET area = ?  WHERE numero_legajo = ?;"
    cursor.execute(sentencia, [area, numero_legajo])
    bd.commit()
    bd.close()
    print("Datos guardados")


def eliminar_registros(cursor, numero_legajo):
    conection_db()
    sentencia = "DELETE FROM empleados WHERE numero_legajo = ?;"
    cursor.execute(sentencia, [numero_legajo])
    bd.commit()
    bd.close()
    print("Datos eliminados")

bd=conection_db()
cursor = bd.cursor()

crear_tabla(cursor)

while True:
    print("ingrese la opcion que desea ejecutar ")
    print("Opción 1: Insertar un registro de empleado")
    print("Opción 2: Seleccionar un registro de empleado a partir de su número de DNI")
    print("Opción 3: Seleccionar todos los empleados o los registros de la tabla")
    print("Opción 4: Modificar el área de un empleado en función de su número de legajo")
    print("Opción 5: Eliminar un empleado a partir de su número de legajo")
    print("Opción 6: Finalizar")
    opcion=input("ingrese la opcion: ")
    if opcion =="1":
        valores=[]
        valor0=int(input("ingrese un id: "))
        valores.append(valor0)
        valor1=int(input("ingrese el numero de legajo "))
        valores.append(valor1)
        valor2=int(input("ingrese el dni: "))
        valores.append(valor2)
        valor3=input("ingrese el nombre: ")
        valores.append(valor3)
        valor4=input("ingrese el apellido: ")
        valores.append(valor4)
        valor5=input("ingrese el area en la que trabaja: ")
        valores.append(valor5)
        
        insertar_nuevo_registro(cursor,valores)    
    elif opcion =="2":
        seleccionar_unregistro(cursor,input("ingrese un dni: "))
        conection_db()
    elif opcion =="3":
        seleccionar_todos_registros(cursor)
        conection_db()
    elif opcion == "4":
        numero_legajo =int(input("ingrese el numero de legajo: "))
        area = input("ingrese la nueva area: ")
        modificar_registros(cursor,numero_legajo,area)
        conection_db()
    elif opcion == "5":
        numero_legajo = int(input("ingrese el numero de legajo: "))
        eliminar_registros(cursor,numero_legajo)
        conection_db()
        
    else :
        bd.close()
        break
    
