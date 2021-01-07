import mysql.connector
# SE ESTABLECE LA CONEXION CON LA BASE DE DATOS PANADERIA_ALL_SWEET
miConexion = mysql.connector.connect(host="localhost", user="root", passwd="Meliodas1999",db="panaderia_all_sweet")
####################################################################################################################################

# Soy Emily
# FUNCION QUE PERMITE OBSERVAR TODOS LOS PRODUCTOS DISPONIBLES PARA EL CLIENTE
def verProductos():
    cur1=miConexion.cursor()
    cur1.execute("select nombre,cantStock,precio,nombreCategoria from producto join categoria on numCategoria=idCategoria")
    print("{:60} {:40} {:20} {:10}".format("Producto","cantidad Estock","precio","categoria"))
    for datos in cur1.fetchall():
        print("{:60} {:40} {:20} {:10}".format(datos[0], str(datos[1]), str(datos[2]), datos[3]))

##################################################################################################################################

# FUNCION PARA INICIAR SESION CLIENTE
def inicioSesionCliente(usuario,contrasena):
    cur3=miConexion.cursor()
    cur3.execute("select usuario, contrasena from cliente")
    for datos in cur3.fetchall():
        if datos[0] == usuario and datos[1]== contrasena:
            return usuario

#################################################################################################################################

# FUNCION PARA INICIAR SESION POR PASTELERO
def inicioSesionPastelero(usuario,contrasena):
    cur3=miConexion.cursor()
    cur3.execute("select usuario, contrasena from pastelero")
    for datos in cur3.fetchall():
        if str(datos[0]) == usuario and str(datos[1])== contrasena:
            return usuario
# FUNCION QUE PERMITE VER LOS PRODUCTOS QUE HA AGREGADO EL PASTELERO

#####################################################################################################################################
def verProductosPastelero(usuario):
    cur3=miConexion.cursor()
    sql = """
    select codProducto, producto.nombre, cantStock, precio, nombreCategoria
    from (pastelero join producto on usuario=usuarioPastelero)join categoria on numCategoria=idCategoria
    where usuarioPastelero='{0}'
    """.format(usuario)
    cur3.execute(sql)

    print("{:60} {:50} {:40} {:30} {:20}".format("codProducto", "nombre producto", "cantidad stock", "precio","categoria"))
    for data in cur3.fetchall():
        print("{:60} {:50} {:40} {:30} {:20}".format(data[0],data[1],str(data[2]), str(data[3]),data[4]))


###############################################################################################################################################
def mostrarPedidos(nombre):
    cur3=miConexion.cursor()
    sql="""
    select codPedido, producto.nombre, estado 
    from (pastelero join producto on usuario=usuarioPastelero) join detalle_pedido on codProducto = cod_producto 
    where pastelero.nombre ='{0}'
    """.format(nombre)

    cur3.execute(sql)

    print("{:60} {:40} {:20} ".format("numero de pedido", "nombre producto", "estado"))
    for data in cur3.fetchall():
        print("{:60} {:40} {:20} ".format(str(data[0]), data[1], data[2]))

def obtenerNombre(usuario):
    cur3=miConexion.cursor()
    cur3.execute("select * from pastelero")
    for nombre in cur3.fetchall():
        if usuario==nombre[0]:
            return nombre[2]




# MENU DE LA APLICACION

print("Sistema de Panaderias All_sweet")
print("1. registrarse")
print("2. iniciar sesion")
print("3. salir")
opcion =0

# MENU PRINCIPAL
while (opcion != 3):
    opcion= int(input("Ingrese una opcion: "))
    if opcion ==1:
        print("xxxx")
        verProductos()
    if opcion==2:

        usuario = input("ingrese su usuario: ")
        contrasena = input("ingrese la contraseña: ")

        if(usuario==inicioSesionCliente(usuario,contrasena)):
            print("ha iniciado sesion con usuario cliente")
            print("1. ver productos disponibles")
            print("2. gestionar compra")
            print("3. fin de sesion")
            nuevaOpcion=0

            # MENU DEL CLIENTE

            while (nuevaOpcion!=3):
                nuevaOpcion = int(input("Ingrese una opcion: "))

                #  VER TODOS LOS PRODUCTOS
                if nuevaOpcion == 1:
                    verProductos()

                if  nuevaOpcion==2:
                    print("zzz")

                # FINALIZAR SESION
                if nuevaOpcion==3:
                    print("ha finalizado sesion correctamente")
        elif(usuario==inicioSesionPastelero(usuario,contrasena)):
            print("ha iniciado sesion con usuario Pastelero")
            print("1. ver productos del dia")
            print("2. ver pedidos y sus productos")
            print("3. fin de sesion")
            nuevaOpcion2 = 0

            # MENU DEL PASTELERO

            while (nuevaOpcion2 != 3):
                nuevaOpcion2 = int(input("Ingrese una opcion: "))

                # VER LOS PRODUCTOS QUE HA AGREGADO EL PASTELERO
                if nuevaOpcion2 == 1:
                    verProductosPastelero(usuario)

                # PEDIDOS QUE PUEDE GESTIONAR EL PASTELERO
                if nuevaOpcion2== 2:
                    nombre= obtenerNombre(usuario)
                    mostrarPedidos(nombre)

                if nuevaOpcion2 == 3:
                    print("ha finalizado sesion correctamente")
    if opcion==3:
        print("gracias por preferirnos vuelva pronto")



miConexion.close()

