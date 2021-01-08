import mysql.connector
# SE ESTABLECE LA CONEXION CON LA BASE DE DATOS PANADERIA_ALL_SWEET
miConexion = mysql.connector.connect(host="localhost", user="root", passwd="Eduybeca8850",db="panaderia_all_sweet")
####################################################################################################################################

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
#######################################################################################################
def obtenerNombre(usuario):
    cur3=miConexion.cursor()
    cur3.execute("select * from pastelero")
    for nombre in cur3.fetchall():
        if usuario==nombre[0]:
            return nombre[2]
####################################################################################################################
def obtenerUsuario(nombre):
    cur4=miConexion.cursor()
    cur4.execute("select * from pastelero")
    for usuario in cur4.fetchall():
        if nombre==usuario[2]:
            return usuario[0]
##########################################################################################################3
def RegistrarCliente():
    usuario = input("ingrese su usuario: ")
    clave = input("ingrese la contraseña: ")
    nombre = input("ingrese nombre: ")
    direccion = input("ingrese direccion: ")
    correo = input("ingrese un correo: ")
    cur3=miConexion.cursor()
    sql="""
    insert into cliente values ('{0}','{1}','{2}','{3}','{4}')""".format(usuario,clave,nombre,direccion,correo)
    cur3.execute(sql)
    miConexion.commit()

#################################################################################################################
def RegistrarPastelero():
    usuario = input("ingrese su usuario: ")
    clave = input("ingrese la contraseña: ")
    nombre = input("ingrese nombre: ")
    direccion = input("ingrese direccion: ")
    correo = input("ingrese un correo: ")
    cur3=miConexion.cursor()
    sql="""
    insert into pastelero values ('{0}','{1}','{2}','{3}','{4}')""".format(usuario,clave,nombre,direccion,correo)
    cur3.execute(sql)
    miConexion.commit()
##################################################################################################################
def aggProducto(codPastelero):
    codProd= input("Ingrese codigo del producto: ")
    nombreProd= input("Ingrese nombre del producto: ")
    cant= input("ingrese la cantidad de productos disponibles: ")
    precio= input("Ingrese el precio del producto: ")
    categoria= input("ingrese la categoria del producto: ")
    cur3=miConexion.cursor()
    sql="""
    insert into producto values('{0}','{1}','{2}','{3}','{4}','{5}',)
    """.format(codProd,nombreProd,cant,precio,categoria,codPastelero)
    cur3.execute(sql)
    miConexion.commit()

##################################################################################################
def verCalificacion(usuario):
    cur3=miConexion.cursor()
    sql="""
    select codCalificacion,puntajeCalProd,puntajePuntualidad,puntajeSaborProd,p.nombre as pastelero,c.fechaCalificacion
    from (calificacion c join cliente cl on c.codigoUsuario=cl.usuario) join pastelero p on c.codigoPastelero=p.usuario
    where codigoUsuario= '{0}' """.format(usuario)
    cur3.execute(sql)
    print("{:60} {:50} {:40} {:30} {:20} {:10} ".format("cod calificacion", "P. CalidadProd", "p. Puntualidad","P. SaborProd","Pastelero","fecha Calificacion"))
    for data in cur3.fetchall():
        print("{:60} {:50} {:40} {:30} {:20} {:10}".format(data[0], str(data[1]), str(data[2]),str(data[3]),data[4],str(data[5])))


#####################################################################################################
def verPasteleros():
    cur4=miConexion.cursor()
    sql="""
    select pastelero.nombre from pastelero order by pastelero.nombre"""
    cur4.execute(sql)
    listaPasteleros=[]
    for data in cur4.fetchall():
        listaPasteleros.append(data[0])
    return listaPasteleros

# MENU DE LA APLICACION

opcion =0

# MENU PRINCIPAL
while (opcion != 3):
    print("Sistema de Panaderias All_sweet")
    print("1. registrarse")
    print("2. iniciar sesion")
    print("3. salir")
    opcion= input("Ingrese una opcion: ")
    if(opcion.isdigit()):
        opcion = int(opcion)
        if opcion ==1:

            registro=0
            while registro!=3:
                print("Para registrarse, digite:")
                print("1. como cliente")
                print("2. como pastelero")
                print("3. regresar")
                registro = input("digite su opcion para el registro: ")
                if registro.isdigit():
                    registro=int(registro)
                    if registro ==1:
                        #verProductos()
                        RegistrarCliente()
                        print("se ha registrado con exito")
                        registro=3
                    if registro ==2:
                        RegistrarPastelero()
                        print("se ha registrado con exito")
                        registro = 3
        if opcion==2:

            usuario = input("ingrese su usuario: ")
            contrasena = input("ingrese la contraseña: ")

            if(usuario==inicioSesionCliente(usuario,contrasena)):

                nuevaOpcion=0

                # MENU DEL CLIENTE

                while (nuevaOpcion!=4):
                    print("ha iniciado sesion con usuario cliente")
                    print("1. ver productos disponibles")
                    print("2. gestionar compra")
                    print("3. ver calificaciones")
                    print("4. fin de sesion")
                    nuevaOpcion =input("Ingrese una opcion: ")


                    #  VER TODOS LOS PRODUCTOS
                    if nuevaOpcion.isdigit():
                        nuevaOpcion=int(nuevaOpcion)
                        if nuevaOpcion == 1:
                            verProductos()

                        if nuevaOpcion==2:

                            for i, info in enumerate(verPasteleros()):
                                print(f"{i}.- {info}")

                            opcionP =input("Escoja  un pastelero: ")
                            if opcionP.isdigit():
                                opcionP=int(opcionP)
                                usuarioP=obtenerUsuario(verPasteleros()[opcionP])
                                print("Pastelero: ", verPasteleros()[opcionP])
                                verProductosPastelero(usuarioP)
                                resp="N"
                                while resp=="S":




                                    resp=input("Desea continuar(S/N): ")


                        if nuevaOpcion==3:
                            verCalificacion(usuario)

                        # FINALIZAR SESION
                        if nuevaOpcion==4:
                            print("ha finalizado sesion correctamente")
            elif(usuario==inicioSesionPastelero(usuario,contrasena)):

                nuevaOpcion2 = 0

                # MENU DEL PASTELERO

                while (nuevaOpcion2 != 4):
                    print("ha iniciado sesion con usuario Pastelero")
                    print("1. ver productos del dia")
                    print("2. ver pedidos y sus productos")
                    print("3. Agregar productos")
                    print("4. fin de sesion")
                    nuevaOpcion2 = input("Ingrese una opcion: ")
                    if nuevaOpcion2.isdigit():
                        nuevaOpcion2=int(nuevaOpcion2)
                    # VER LOS PRODUCTOS QUE HA AGREGADO EL PASTELERO
                        if nuevaOpcion2 == 1:
                            verProductosPastelero(usuario)

                        # PEDIDOS QUE PUEDE GESTIONAR EL PASTELERO
                        if nuevaOpcion2== 2:
                            nombre= obtenerNombre(usuario)
                            mostrarPedidos(nombre)

                        if nuevaOpcion2 == 3:
                            aggProducto(usuario)
                            print("Se ha agregado el producto exitosamente")

                        if nuevaOpcion2 == 4:
                            print("ha finalizado sesion correctamente")

        if opcion==3:
            print("gracias por preferirnos vuelva pronto")





miConexion.close()