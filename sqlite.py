import sqlite3
#coneccion a la base de datos a partir de un objeto conection
bd = sqlite3.connect("example.db")
print("base de datos abierta")
#crear una tabla a partir del metodo cursor
cursor =bd.cursor()
cursor.execute('''CREATE TABLE  IF NOT  EXISTS stocks
            (date text,trans text ,symbol text,qty real,price real)''')
#la mayoria de las manupulaciones de una base de datos son a partir de un metodo execute
#insertar un registro por ejemplo
cursor.execute("INSERT INTO stocks VALUES('2020-01-05','buy','RHAT',100,35.14)")
#guardar los cambios
bd.commit()
#se recomiendan cerrar la conexion con 
#bd.close()
#seleccionar los registros de una tabla
#bd = sqlite3.connect("example.db")
t=('RHAT',)
cursor.execute('SELECT * FROM stocks WHERE symbol = ? ',t)
print(cursor.fetchone())
#fetchone selecciona el primero ,fethall seleccione todo
#ejemplo con un iterador
for row in cursor.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

#eliminar datos de una tabla
'''symbol ='SONY'
sentencia ="DELETE FROM stocks WHERE symbol = ?;"
cursor.execute(sentencia,[symbol])
bd.commit()
print("eliminado con exito")'''

#para actualizar datos
qty = 1500
price =85.00
symbol ='MSFT'
sentencia = "UPDATE stocks SET qty = ?,price = ? WHERE symbol = ?"
cursor.execute(sentencia,[qty,price,symbol])
bd.commit()
print("datos guardados")