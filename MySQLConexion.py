import mysql.connector



conexion = mysql.connector.connect(user='root', password='123456789',
                                   host='localhost', database='codificador',
                                   port='3306')


print(conexion)

cursor = conexion.cursor()

cursor.execute("SELECT database();")
registro = cursor.fetchone()
print("Conectado a la DB: ", registro)

def agregarDatosSQL(con, sinCon):
    sql = "INSERT INTO passwords (Pass_Value, Pass_Original) VALUES (%s, %s)"
    val = (str(con), str(sinCon))
    cursor.execute(sql, val)

    conexion.commit()


#def imprimirDatosSQL(con):


sql = "SELECT * FROM passwords WHERE Pass_Original ='%s' "

cursor.execute(sql)

resultados = cursor.fetchall()



print(resultados[0][1])







