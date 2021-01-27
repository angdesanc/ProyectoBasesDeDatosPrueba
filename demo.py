import numpy as np
from datetime import date
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
def obtenerNombreP(usuario):
    cur3=miConexion.cursor()
    cur3.execute("select * from pastelero")
    for nombre in cur3.fetchall():
        if usuario==nombre[0]:
            return nombre[2]
####################################################################################################################
def obtenerUsuarioP(nombre):
    cur4=miConexion.cursor()
    cur4.execute("select * from pastelero")
    for usuario in cur4.fetchall():
        if nombre==usuario[2]:
            return usuario[0]
##########################################################################################################
def obtenerNombreC(usuario):
    cur3=miConexion.cursor()
    cur3.execute("select * from cliente")
    for nombre in cur3.fetchall():
        if usuario==nombre[0]:
            return nombre[2]
####################################################################################################################
def obtenerUsuarioC(nombre):
    cur4=miConexion.cursor()
    cur4.execute("select * from cliente")
    for usuario in cur4.fetchall():
        if nombre==usuario[2]:
            return usuario[0]
##########################################################################################################
def RegistrarCliente():
    usuario = input("ingrese su usuario: ")
    clave = input("ingrese la contraseña: ")
    nombre = input("ingrese nombre: ")
    direccion = input("ingrese direccion: ")
    correo = input("ingrese un correo: ")
    while ('@'not in correo):
        print('Él correo no es valido.')
        correo = input('Ingrese un correo: ')
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
    while ('@'not in correo):
        print('Él correo no es valido.')
        correo = input('Ingrese un correo: ')
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
    while not (cant.isdigit()):
        print('Cantidad incorrecta')
        cant=input('Ingrese la cantidad delproducto disponible: ')
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

#########################################################################################################
def verProductosPasteleroLista(usuario):
    Lista=[]
    cur3=miConexion.cursor()
    sql = """
    select codProducto, producto.nombre, cantStock, precio, nombreCategoria
    from (pastelero join producto on usuario=usuarioPastelero)join categoria on numCategoria=idCategoria
    where usuarioPastelero='{0}'
    """.format(usuario)
    cur3.execute(sql)
    for data in cur3.fetchall():
        Lista.append(list(data))
    return Lista
########################################################################################################
ListaAL=[]
def elegirProductos():

    for i, info in enumerate(verPasteleros()):
        print(f"{i}.- {info}")

    opcionP = input("Escoja  un pastelero: ")
    while not (opcionP.isdigit()):
        print('No existe pastelero. Intente de nuevo.')
        opcionP=input('Esccoja un pastelero: ')

    opcionP = int(opcionP)
    usuarioP = obtenerUsuarioP(verPasteleros()[opcionP])
    print("Pastelero: ", verPasteleros()[opcionP])
    verProductosPastelero(usuarioP)
    lista_usar=verProductosPasteleroLista(usuarioP)
    solPed=input("Desea realizar un pedido?(S/N): ").upper()
    while not (solPed =='S' or solPed =='N'):
        print('Opcion incorrecta. Intente de nnuevo')
        solPed = input("Desea realizar un pedido?(S/N): ").upper()
    if solPed=="S":
        resp="S"
        while resp!="N":
            listaProdPastInt = []
            codp_cant=input("Ingrese codigo del producto y la cantidad separado por una coma:")
            cod, cant=codp_cant.split(",")

            for i in lista_usar:
                if i[0]==cod:
                    listaProdPastInt.append(cod)
                    listaProdPastInt.append(i[3])
                    listaProdPastInt.append(int(cant))
                    listaProdPastInt.append(float("%.2f"%(i[3]*int(cant))))
                    ListaAL.append(listaProdPastInt)
            resp=input("Desea agregar otro producto?(S/N): ").upper()
        print("Su pedido se ha generado con éxito")
        print("Creacion de factura")
        nombreC = input("Ingrese su nombre:")
        envio = input("Desea envío(S/N): ").upper()
        metodoPago = input("Ingrese su método de pago: ")
        datosFact = crearFactura(nombreC, envio, metodoPago)
        pedido = creaPedido(datosFact, usuario)
        detallePedido(ListaAL, pedido)
    else:
        print("Gracia vuelva pronto.")
#########################################################################################
def crearFactura(nombre,envio, metodoPago):
    datosfact=[]
    cur3 = miConexion.cursor()
    sql = """
        select numFactura from factura order by numFactura;
        """
    cur3.execute(sql)
    codigosLista=[]
    for data in cur3.fetchall():
        for datainter in data:
            codigosLista.append(datainter)
    valorCod=codigosLista[-1]+1
    datosfact.append(str(valorCod))
    fecha= date.today()
    datosfact.append(str(fecha))
    #for i, info in enumerate(ListaAL):
    datosBackup=[]   #   ["cod1,10,2,3","cod2,2,5,6"]
    for i in ListaAL:
        x= str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])
        datosBackup.append(x)

    detalle=",".join(datosBackup)
    datosfact.append(detalle)



    subtotal=0
    for j, infoj in enumerate(ListaAL):
        subtotal+=infoj[3]

    datosfact.append(str(subtotal))
    if envio=="S":

        valorTotal = "%.2f"%(((subtotal*0.12)+subtotal)+5)
        datosfact.append(str(valorTotal))
        datosfact.append(str(5))
    else:

        valorTotal="%.2f"%((subtotal*0.12)+subtotal)
        datosfact.append(str(valorTotal))
        datosfact.append(str(0))
    datosfact.append(str(metodoPago))
    datosfact.append(str(obtenerUsuarioC(nombre)))
    datosfact.append(str(1))
    print(datosfact)
    cur3=miConexion.cursor()
    sql="""
    insert into factura values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')
    """.format(str(datosfact[0]),str(datosfact[1]),str(datosfact[2]),str(datosfact[3]), str(datosfact[4]),str(datosfact[5]),str(datosfact[6]),str(datosfact[7]), datosfact[8])
    cur3.execute(sql)
    miConexion.commit()
    return datosfact

def creaPedido(factura, usuario):
    cur3 = miConexion.cursor()
    sql = """
            select noPedido from pedido order by noPedido;
            """
    cur3.execute(sql)
    noPedidosLista = []
    for data in cur3.fetchall():
        for datainter in data:
            noPedidosLista.append(datainter)
    valorNo = noPedidosLista[-1] + 1
    numPedido=str(valorNo)
    cur3=miConexion.cursor()
    sql="""insert into pedido values ('{0}','{1}','{2}')
    """.format(numPedido,usuario,str(factura[0]))
    cur3.execute(sql)
    miConexion.commit()
    return numPedido

def detallePedido(listaAll,pedido):
    estado="en espera"
    codPro=""
    cant=""
    cur3=miConexion.cursor()
    for i in listaAll:
        codPro=i[0]
        cant=str(i[2])
        sql = """insert into detalle_pedido values ('{0}','{1}','{2}','{3}')
            """.format(cant, estado, codPro,pedido)
        cur3.execute(sql)
        miConexion.commit()

# MENU DE LA APLICACION

opcion =0

# MENU PRINCIPAL
while (opcion != 3):
    print("Sistema de Panaderias All_sweet")
    print("1. registrarse")
    print("2. iniciar sesion")
    print("3. salir")
    opcion= input("Ingrese una opcion: ")
    while (not opcion.isdigit()) or 1>int(opcion) or int(opcion)>3:
        print('Opcion no valida. Intente de nuevo.')
        opcion = input("Ingrese una opcion: ")
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
                            elegirProductos()


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
                            nombre= obtenerNombreP(usuario)
                            mostrarPedidos(nombre)

                        if nuevaOpcion2 == 3:
                            aggProducto(usuario)
                            print("Se ha agregado el producto exitosamente")

                        if nuevaOpcion2 == 4:
                            print("ha finalizado sesion correctamente")

        if opcion==3:
            print("gracias por preferirnos vuelva pronto")





miConexion.close()