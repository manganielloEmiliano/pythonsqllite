import sqlite3

def conection_db():
    bd = sqlite3.connect("Empleados.db")
    return bd, bd.cursor()

def crear_tabla():
    bd,cursor = conection_db()
    cursor.execute('''CREATE TABLE  IF NOT  EXISTS empleados (
	"id"	INTEGER NOT NULL,
	"numero_legajo"	INTEGER NOT NULL UNIQUE,
    "dni"	INTEGER NOT NULL UNIQUE,
	"nombre_empleado"	TEXT NOT NULL,
	"apellido_empleado"	TEXT NOT NULL,
	"area"	TEXT NOT NULL,
	PRIMARY KEY("id"AUTOINCREMENT));''')


def insertar_nuevo_registro(valores):
    bd,cursor = conection_db()
    cursor.execute("INSERT INTO empleados(numero_legajo,dni,nombre_empleado) VALUES(?,?,?,?,?)", valores)
    bd.commit()
    bd.close()


def seleccionar_unregistro(dni):
    bd,cursor = conection_db()
    cursor.execute('SELECT * FROM empleados WHERE dni=?', [dni])
    print(cursor.fetchone())


def seleccionar_todos_registros():
    db,cursor = conection_db()
    cursor.execute('SELECT * FROM empleados',)
    
    #recorrer los registros
    lista = cursor.fetchall()
    for registro in lista:
        print(registro[2])
    ###########
    db.commit()
    db.close()


def modificar_registros(numero_legajo, area):
    bd,cursor = conection_db()
    sentencia = "UPDATE empleados SET area = ?  WHERE numero_legajo = ?;"
    cursor.execute(sentencia, [area, numero_legajo])
    bd.commit()
    bd.close()
    print("el area de trabajo del empleado con el legajo {} fue actualizada a{}".format(
        numero_legajo, area))


def eliminar_registros(numero_legajo):
    bd,cursor = conection_db()
    sentencia = "DELETE FROM empleados WHERE numero_legajo = ?;"
    cursor.execute(sentencia, [numero_legajo])
    bd.commit()
    bd.close()
    print("Datos eliminados")