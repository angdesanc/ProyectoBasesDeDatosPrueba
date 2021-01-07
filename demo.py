import mysql.connector
# SE ESTABLECE LA CONEXION CON LA BASE DE DATOS PANADERIA_ALL_SWEET
miConexion = mysql.connector.connect(host="localhost", user="root", passwd="Meliodas1999",db="panaderia_all_sweet")
cur1=miConexion.cursor()
cur1.execute("select nombre,cantStock,precio,nombreCategoria from producto join categoria on numCategoria=idCategoria")
print("{:60} {:40} {:20} {:10}".format("Producto","cantidad Estock","precio","categoria"))
for datos in cur1.fetchall():
    print("{:60} {:40} {:20} {:10}".format(datos[0], str(datos[1]), str(datos[2]), datos[3]))
