create table pastelero(
	usuario varchar(30) not null,
    contrasena varchar(30) not null,
    nombre varchar(50) not null,
    direccion varchar(50) not null,
    correo varchar(45) default null,
    primary key(usuario));
    
-- se agrega 10 pasteleros
INSERT INTO pastelero values ("1000","pastelero1","Jesus Dominguez","av. Fco de Orellana","jsdom@gmail.com");
INSERT INTO pastelero values ("1001","pastelero2","Jaime Perez","av. Juan tanca marengo","jupz@gmail.com");
INSERT INTO pastelero values ("1002","pastelero3","Pedro Gonzales","av. 9 de Octubre","pdgonz@gmail.com");
INSERT INTO pastelero values ("1003","pastelero4","Damian Diaz","av. Domingo Comin","dadiz@gmail.com");
INSERT INTO pastelero values ("1004","pastelero5","Derian Vizuete","av. Simon Bolivar","devie@gmail.com");
INSERT INTO pastelero values ("1005","pastelero6","David Oyarvide","av. Las Americas","Daoyade@gmail.com");
INSERT INTO pastelero values ("1006","pastelero7","Emily Cordero","av. Barcelona","emily99@gmail.com");
INSERT INTO pastelero values ("1007","pastelero8","Dayse Fernandez","av. Alban Borja","daysefer00@gmail.com");
INSERT INTO pastelero values ("1008","pastelero9","Karen Benitez","av. 10 de agosto ","karito97@gmail.com");
INSERT INTO pastelero values ("1009","pastelero10","Claudia Gonzales","av. Carlos Julio Arosemena","clauzal99@gmail.com");


-- creacion de tabla pasteleria
create table pasteleria(
	idPasteleria varchar(30) not null,
    direccion varchar(50) not null,
    nombre varchar(30) not null,
    ciudad varchar(30) not null,
    usuarioPastelero varchar(30) not null,
    primary key(idPasteleria),
    foreign key(usuarioPastelero) references pastelero(usuario));

-- creacion de registros de pastelerias 

insert into pasteleria values ("past001","av juan tanca marengo","Dulcesitos SA","Guayaquil","1000");
insert into pasteleria values ("past002","av Francisco de orellana","Panes SA","Guayaquil","1001");
insert into pasteleria values ("past003","av Francisco de orellana","Esquinita del sabor","Guayaquil","1002");
insert into pasteleria values ("past004","av Las Americas","La favorita","Guayaquil","1003");
insert into pasteleria values ("past005","av Machala y Gomez Rendon","California","Guayaquil","1004");
insert into pasteleria values ("past006","av 9 de Octubre","Paseteles doña Merced","Guayaquil","1005");
insert into pasteleria values ("past007","av Simon Bolivar","Panaderia don Julio","Guayaquil","1006");
insert into pasteleria values ("past008","av 25 de Julio","Dulces tu sabor","Guayaquil","1007");
insert into pasteleria values ("past009","av Jaime Roldos Aguilera","Pasteleria don Vito","Guayaquil","1008");
insert into pasteleria values ("past010","av Francisco de orellana","Pasteleria Jesus Andrade","Guayaquil","1009");

-- creacion de la tabla categorias.
create table categoria(
	idCategoria varchar(30) not null,
    nombreCategoria varchar(40) not null,
    primary key (idCategoria));

-- insercion de 5 categorias.
insert into categoria values ("cat00", "Bizcochos");
insert into categoria values ("cat01", "Dulces");
insert into categoria values ("cat02", "Panes");
insert into categoria values ("cat03", "tortas");
insert into categoria values ("cat04", "productos de sal");
insert into categoria values ("cat05", "bebidas con cafe");
insert into categoria values ("cat06","Gelatinas");
insert into categoria values ("cat07", "Flanes");
insert into categoria values ("cat08", "Galletas");
insert into categoria values ("cat09", "jugos y bebidas embotelladas");

-- creacion de tabla productos
create table producto(
	codProducto varchar(30) not null,
    nombre varchar(50) not null,
    cantStock int not null,
    precio double not null,
    numCategoria varchar(309) not null,
    usuarioPastelero varchar(30) not null,
    primary key (codProducto),
    foreign key (numCategoria) REFERENCES categoria(idCategoria),
    foreign key (usuarioPastelero) REFERENCES pastelero(usuario));


-- bizcochos
insert into producto values("prod00","mojada de Chocolate",10, 3.50,"cat00","1001");
insert into producto values("prod01","torta de naranja",5, 5.50,"cat00","1001");
-- dulces
insert into producto values("prod02","dulce de Cuatro Leches",4, 6.25,"cat01","1002");
insert into producto values("prod03","dulce de tres leches",8, 4.30,"cat01","1002");
-- panes 02
insert into producto values("prod04","cara sucia",20, 0.25,"cat02","1003");
insert into producto values("prod05","empanada de queso",20, 0.30,"cat02","1003");
-- tortas 03
insert into producto values("prod06","torta de Manzana y Nuez",10, 10.25,"cat03","1004");
insert into producto values("prod07","Cheesecake",10, 12.25,"cat03","1004");
-- productos de sal 04
insert into producto values("prod08","humitas",30, 1.25,"cat04","1005");
insert into producto values("prod09","torta de choclo",20, 2.60,"cat04","1005");
-- bebidas con cafe 05
insert into producto values("prod10","expreso",50, 1.00,"cat05","1006");
insert into producto values("prod11","Americano",50, 1.35,"cat05","1006");
-- gelatinas 06
insert into producto values("prod12","gelatina vino tinto",20,10.50,"cat06","1007");
-- flanes 07
insert into producto values("prod13","flan de queso",20, 2.25,"cat07","1007");
insert into producto values("prod14","flan de chocolate",30, 2.55,"cat07","1008");
-- galletas 08
insert into producto values("prod15","otap",20, 2.40,"cat08","1008");
insert into producto values("prod16","avena con pasas",20, 3.15,"cat08","1009");
-- jugos y bebidas embotelladas 09
insert into producto values("prod17","jugo cold naranja",60, 1.25,"cat09","1009");
insert into producto values("prod18","coca cola regular",50, 1.00,"cat09","1008");
insert into producto values("prod19","coca cola light",40, 1.25,"cat09","1002");


-- creacion de la tabla cliente

CREATE TABLE cliente(
usuario varchar(30)  NOT NULL,
PRIMARY KEY (usuario),
contrasena varchar(50) NOT NULL,
nombre varchar(50) NOT NULL,
direccion varchar(50) NOT NULL, 
correo varchar(50) default NULL);

-- registro de clientes
INSERT INTO Cliente VALUES ('clie1000','1234567','Angello Saltos','MuchoLote 2, Mz. 54 Villa 2','angellosaltos01@outlook.com');
INSERT INTO Cliente VALUES ('clie1001','hola123','Camila Lopez','Urb. La Joya, Etapa Zafiro, Mz.12 Villa 11','camlopez04@gmail.com');
INSERT INTO Cliente VALUES ('clie1002','chao1234','Nicole Estevez','Sauces IV, Mz. 23 Villa 3','angieeq@gmail.com');
INSERT INTO Cliente VALUES ('clie1003','kimkardashian','Fabiana Huacon','Aguirre 523 y Escobedo','fbhuacon@gmail.com');
INSERT INTO Cliente VALUES ('clie1004','qwertyuio123','Nidia Sabando','Clemente Ballen 622 y Garcia Aviles','nidiacorsab@outlook.com');
INSERT INTO Cliente VALUES ('clie1005','anita345','Ana Paula Enriquez','Capitan Zaera y Colombia','anapaulaeb@gmail.com');
INSERT INTO Cliente VALUES ('clie1006','asdfgh00','Juan Franco','Sauces IV, Mz.14 Villa 9','juanfrancisco@gmail.com');
INSERT INTO Cliente VALUES ('clie1007','2325560','Roberto Cornejo','Cdla. El condor, Calle Base sur, Mz.15 Villa 1','corneroberto@hotmail.com');
INSERT INTO Cliente VALUES ('clie1008','2425235','Melissa Moran','Urb. Castilla Mz.54 Villa 20','mmoran01@hotmail.com');
INSERT INTO Cliente VALUES ('clie1009','jueves2508','Patricio Viteri','Boyaca 624 y Padre Solano','viteri25patri@outlook.com');


-- creacion de tabla de calificacion
create table calificacion(
	codCalificacion varchar(30) not null,
	puntajeCalProd int not null,
    puntajePuntualidad int not null,
    puntajeSaborProd int not null,
    codigoPastelero varchar(30) not null,
    codigoUsuario varchar(30) not null,
    fechaCalificacion date not null,
    check(puntajeCalProd>0 and puntajeCalProd<11),
    check(puntajePuntualidad>0 and puntajePuntualidad<11),
    check(puntajeSaborProd>0 and puntajeSaborProd<11),
    primary key(codCalificacion),
    foreign key (codigoPastelero) references pastelero(usuario),
    foreign key (codigoUsuario) references cliente(usuario));


-- registro calificaciones
INSERT INTO calificacion values("cal000",8,9,10,"1000","clie1000","2020-05-15");
INSERT INTO calificacion values("cal001",7,5,8,"1000","clie1003","2020-05-15");
INSERT INTO calificacion values("cal002",9,6,7,"1001","clie1000","2020-10-12");
INSERT INTO calificacion values("cal003",4,9,10,"1002","clie1001","2020-01-20");
INSERT INTO calificacion values("cal004",6,7,8,"1000","clie1002","2020-05-15");
INSERT INTO calificacion values("cal005",7,9,8,"1004","clie1003","2020-03-15");
INSERT INTO calificacion values("cal006",5,8,10,"1005","clie1004","2020-04-21");
INSERT INTO calificacion values("cal007",9,9,10,"1000","clie1005","2020-05-15");
INSERT INTO calificacion values("cal008",9,5,10,"1007","clie1006","2020-07-05");
INSERT INTO calificacion values("cal009",9,10,10,"1008","clie1007","2020-08-26");
INSERT INTO calificacion values("cal010",8,7,10,"1009","clie1009","2015-11-17");


-- creacion de la tabla tarjeta

CREATE TABLE Tarjeta(
noTarjeta varchar(16),
PRIMARY KEY (noTarjeta),
banco varchar(45) NOT NULL,
tipoTarjeta varchar(45) NOT NULL,
usuarioCliente varchar(50) NOT NULL,
KEY(usuarioCliente),
FOREIGN KEY (usuarioCliente) REFERENCES Cliente (usuario));




-- creacion de la tabla telefono

CREATE TABLE Telefono(
telefono varchar(30) NOT NULL,
PRIMARY KEY (telefono),
Cliente_usuario varchar(30) NOT NULL,
FOREIGN KEY (cliente_usuario) REFERENCES Cliente (usuario));


-- registros de telefonos
INSERT INTO telefono Values ('0982442262','clie1000');
INSERT INTO telefono Values ('0982465811','clie1001');
INSERT INTO telefono Values ('0912345678','clie1002');
INSERT INTO telefono Values ('0951665823','clie1003');
INSERT INTO telefono Values ('0986655262','clie1004');
INSERT INTO telefono Values ('0982468255','clie1005');
INSERT INTO telefono Values ('0982004952','clie1006');
INSERT INTO telefono Values ('0966118504','clie1007');
INSERT INTO telefono Values ('0983332245','clie1008');
INSERT INTO telefono Values ('0982499214','clie1009');



-- registro de tarjetas
INSERT INTO Tarjeta VALUES ('1234567890123456','Banco Pichincha','debito','clie1000');
INSERT INTO Tarjeta VALUES ('1002456285963255','Banco Pichincha','credito','clie1002');
INSERT INTO Tarjeta VALUES ('4023455125635109','Banco ProduBanco','debito','clie1002');
INSERT INTO Tarjeta VALUES ('9653184469235569','Banco Solidario','debito','clie1003');
INSERT INTO Tarjeta VALUES ('9561253890123456','Banco Pichincha','debito','clie1005');
INSERT INTO Tarjeta VALUES ('1784526345229866','Banco Guayaquil','debito','clie1006');
INSERT INTO Tarjeta VALUES ('2031879658845456','Banco Guayaquil','debito','clie1007');
INSERT INTO Tarjeta VALUES ('1478520369874120','Banco Internacional','credito','clie1007');
INSERT INTO Tarjeta VALUES ('3698745120152469','Banco Del Bank','debito','clie1008');
INSERT INTO Tarjeta VALUES ('8520123654789632','Banco Pichincha','credito','clie1009');


-- creacion de la tabla factura
CREATE TABLE Factura(
numFactura int NOT NULL,
PRIMARY KEY (numFactura),
fechaFactura date NOT NULL,
detalle varchar(80) NOT NULL,
subtotal double NOT NULL,
valorTotal double NOT NULL,
recargoEnvio double,
metodoPago varchar(45) NOT NULL,
codCliente varchar(50) NOT NULL,
estadoFac boolean not null, 
FOREIGN KEY (codCliente) REFERENCES Cliente (usuario));


-- registro factura
INSERT INTO Factura 
VALUES (101,'2020-11-20','16 cara sucia-20 empanada de queso',10.00,16.20,5.00,'efectivo','clie1002',0);
INSERT INTO Factura 
VALUES (102,'2020-10-1' ,'3 Americano',4.05,4.54,0,'efectivo','clie1000',1);
INSERT INTO Factura 
VALUES (103,'2020-10-1' ,'5 torta de choclo-12 humitas',28.00,36.36,5.00,'tarjeta de debito','clie1005',1);
INSERT INTO Factura 
VALUES (104,'2020-11-6' ,'1 cheesecake',12.25,18.72,5.00,'tarjeta de credito','clie1005',1);
INSERT INTO Factura 
VALUES (105,'2020-10-22' ,'2 dulce de cuatro leches',12.50,14.00,0,'tarjeta de debito','clie1006',1);
INSERT INTO Factura 
VALUES (106,'2020-11-8' ,'3 porciones de torta de choclo',7.80,8.74,0,'efectivo','clie1004',1);
INSERT INTO Factura 
VALUES (107,'2020-10-20' ,'1 torta de Manzana y nuez',10.25,16.48,5.00,'tarjeta de debito','clie1008',1);
INSERT INTO Factura 
VALUES (108,'2020-10-6' ,'14 avena con pasas',44.10,54.4,5.00,'tarjeta de debito','clie1007',1);
INSERT INTO Factura 
VALUES (109,'2020-10-11' ,'2 dulce de tres leches, 1 coca cola light',9.85,16.03,5.00,'tarjeta de credito','clie1009',1);
INSERT INTO Factura 
VALUES (110,'2020-10-15' ,'1 cheesecake',12.25,14.00,0,'efectivo','clie1005',1);
INSERT INTO 
Factura VALUES (111,'2020-11-20','Personalizado_8-Personalizado_9-Personalizado_10',56.00,67.72,5.00,'efectivo','clie1001',0);
INSERT INTO Factura 
VALUES (112,'2020-11-18','Personalizado_4-Personsalizado_5',43.1,53.27,5.00,'tarjeta de debito','clie1004',1);
INSERT INTO Factura 
VALUES (113,'2020-11-17','Personalizado_1-Personalizado_2-Personalizado_3-6 coca cola light',78.00,92.36,5.00,'tarjeta de credito','clie1009',1);
INSERT INTO Factura 
VALUES (114,'2020-11-19','Personalizado_6-Personalizado_7-5 humitas',21.85,29.47,5.00,'tarjeta de debito','clie1003',1);

-- creacion de la tabla pedido

CREATE TABLE PEDIDO(
	noPedido int not null,
    usuarioCliente varchar(30) not null,
    codFactura int not null,
    primary key(noPedido),
    foreign key(usuarioCliente) references cliente(usuario),
    foreign key(codFactura) references factura(numFactura));

-- registro pedidos
INSERT INTO Pedido VALUES (21,'clie1002',101);
INSERT INTO Pedido VALUES (16,'clie1000',102);
INSERT INTO Pedido VALUES (17,'clie1005',103);
INSERT INTO Pedido VALUES (20,'clie1005',104);
INSERT INTO Pedido VALUES (25,'clie1006',105);
INSERT INTO Pedido VALUES (26,'clie1004',106);
INSERT INTO Pedido VALUES (27,'clie1008',107);
INSERT INTO Pedido VALUES (28,'clie1007',108);
INSERT INTO Pedido VALUES (29,'clie1009',109);
INSERT INTO Pedido VALUES (30,'clie1005',110);
INSERT INTO Pedido VALUES (37,'clie1001',111);
INSERT INTO Pedido VALUES (32,'clie1004',112);
INSERT INTO Pedido VALUES (33,'clie1009',113);
INSERT INTO Pedido VALUES (36,'clie1003',114);


-- creacion de la tabla detalle pedido
create table detalle_pedido(
	cantidadProd int not null,
    estado varchar(30) not null,
    cod_producto varchar(30) not null,
    codPedido int not null,
    check(estado="en espera" or estado="entregado"),
    primary key (cod_producto, codPedido),
    foreign key (cod_producto) references producto(codProducto),
    foreign key (codPedido) references pedido(noPedido));

-- registros de detalle pedido

insert into detalle_pedido values(16, 'en espera', 'prod04', 21);
insert into detalle_pedido values(20, 'entregado', 'prod05', 21);
insert into detalle_pedido values(3, 'entregado', 'prod11', 16);
insert into detalle_pedido values(5, 'entregado', 'prod09', 17);
insert into detalle_pedido values(12, 'entregado', 'prod08', 17);
insert into detalle_pedido values(1, 'entregado', 'prod07', 20);
insert into detalle_pedido values(2, 'entregado', 'prod02', 25);
insert into detalle_pedido values(3, 'entregado', 'prod09', 26);
insert into detalle_pedido values(1, 'entregado', 'prod06',27);
insert into detalle_pedido values(14, 'entregado', 'prod16', 28);
insert into detalle_pedido values(2, 'entregado', 'prod03', 29);
insert into detalle_pedido values(1, 'entregado', 'prod19', 29);
insert into detalle_pedido values(1, 'entregado', 'prod07', 30);




-- creacion de tabla producto personalizado
CREATE TABLE Producto_Personalizado(
noProdPer int  NOT NULL,
PRIMARY KEY (noProdPer),
cantidad int NOT NULL,
descripcion varchar(45) NOT NULL,
sabor varchar(30) NOT NULL,
decoracion varchar(45),
porciones int,
precioUnid double NOT NULL,
id_pedido int NOT NULL,
id_pastelero varchar(30),
FOREIGN KEY (id_pedido) REFERENCES Pedido (noPedido),
FOREIGN KEY (id_pastelero) REFERENCES Pastelero (usuario));


-- registros de producto personalizado
INSERT INTO Producto_personalizado 
VALUES(1,1,'pastel de 2 pisos','chocolate','manga pastelera',40,22.50,33,'1002');
INSERT INTO Producto_personalizado 
VALUES(2,30,'galletas redondas grandes','mantequilla avellanada','diseños de Navidad',null,0.40,33,'1002');
INSERT INTO Producto_personalizado 
VALUES(3,30,'cupcakes medianos','red velvet','figuras de fondant Papá Noel',null,1.20,33,'1002');
INSERT INTO Producto_personalizado 
VALUES(4,1,'postre mil hojas','manjar',null,20,12.00,32,'1008');
INSERT INTO Producto_personalizado 
VALUES(5,6,'rollitos de canela','canela dulce','glaseado de azucar',null,0.60,32,'1008');
INSERT INTO Producto_personalizado 
VALUES(6,1,'porciones de cheesecake','oreo',null,17,2.30,36,'1005');
INSERT INTO Producto_personalizado 
VALUES(7,40,'rollos de manjar','manjar de leche',null,null,0.10,36,'1005');
INSERT INTO Producto_personalizado 
VALUES(8,1,'Torta cuadrada de 1 piso','vainilla','Diseño de Frozen',25,18.00,37,'1006');
INSERT INTO Producto_personalizado 
VALUES(9,20,'cupcakes medianos','chocolate blanco y almendras','azucar como copos de nieve',null,1.40,37,'1006');
INSERT INTO Producto_personalizado 
VALUES(10,20,'Brownies pequeños','chocolate con almendras',null,null,0.50,37,'1006');



-- creacion de la tabla envio

CREATE TABLE Envio(
noEnvio int NOT NULL,
PRIMARY KEY (noEnvio),
fechaEnvio date NOT NULL,
horaSalidaGlovo time NOT NULL,
horaLlegadaGlovo time NOT NULL,
retiraEfectivo boolean NOT NULL,
pedido_noPedido int NOT NULL, 
FOREIGN KEY (pedido_noPedido) REFERENCES Pedido (noPedido));


-- creacion de la tabla domicilio

CREATE TABLE Domicilio(
Envio_noEnvio INT NOT NULL,
PRIMARY KEY (Envio_noEnvio),
FOREIGN KEY (Envio_noEnvio) REFERENCES Envio (noEnvio),
codigoPostal varchar(45) NOT NULL,
callePrimaria varchar(45) NOT NULL,
calleSecundaria varchar(45) NOT NULL
);

-- registros de envios

INSERT INTO Envio 
VALUES (2,'2020-10-1','12:00:00','12:20:00',0,17);
INSERT INTO Envio 
VALUES (11,'2020-11-6','18:10:00','18:27:00',0,20);
INSERT INTO Envio 
VALUES (9,'2020-10-20','9:33:00','10:00:00',0,27);
INSERT INTO Envio 
VALUES (5,'2020-10-6','11:18:00','11:34:00',0,28);
INSERT INTO Envio 
VALUES (8,'2020-10-11','8:15:00','8:29:00',0,29);
INSERT INTO Envio 
VALUES (16,'2020-11-20','19:12:00','19:35:00',1,37);
INSERT INTO Envio 
VALUES (13,'2020-11-18','10:22:00','10:50:00',0,32);
INSERT INTO Envio 
VALUES (12,'2020-11-17','9:42:00','9:58:00',0,33);
INSERT INTO Envio 
VALUES (14,'2020-11-19','13:55:00','14:13:00',0,36);
insert into envio 
values (15, '2020-11-20','16:08:00','16:40:00',1,21);
 
-- domicilio
INSERT INTO Domicilio VALUES (15,'090101','MuchoLote 2, calle Los Lirios','Mz.54 Villa 2');
INSERT INTO Domicilio VALUES (2,'090102', 'francisco de orellana', 'orquideas mz15 villa 3');
INSERT INTO Domicilio VALUES (11,'090111', 'via perimetral', 'las cumbres mz 3 villa 2');
INSERT INTO Domicilio VALUES (9,'090203', 'via daule', 'pascuales mz 1234 villa 3');
INSERT INTO Domicilio VALUES (5,'090111', 'malecon simon bolivar', 'diez de agosto');
INSERT INTO Domicilio VALUES (8,'090150', 'rumichaca', '25 y portete');
INSERT INTO Domicilio VALUES (16,'090104', '6 de marzo', '3 de octubre');
INSERT INTO Domicilio VALUES (13,'090108', 'colonial panamá', '9 de octubre');
INSERT INTO Domicilio VALUES (12,'090302', 'avenida de las americas', 'urdesa central');
INSERT INTO Domicilio VALUES (14,'090305', '25 de julio', 'calle el oro');



                  




 






















    




    







    
    