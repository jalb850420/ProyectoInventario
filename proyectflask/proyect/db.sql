CREATE TABLE Usuarios (
    id      VARCHAR (15)    PRIMARY KEY 
                            NOT NULL,
    nombre  CHAR (50),
    mail    CHAR (50),
    perfil  CHAR (15),
    usuario CHAR (20),
    passw   CHAR (20) 
);

CREATE TABLE Productos (
    id_producto    VARCHAR (15) PRIMARY KEY
                                NOT NULL,
    nombre         CHAR (30),
    marca          CHAR (20),
    descripcion    CHAR (50),
    categoria      CHAR (15),
    costo          DOUBLE,
    precio         DOUBLE,
    cantidad       DOUBLE,
    id_proveedores VARCHAR (15) REFERENCES Proveedores (id_proveedores) 
                                NOT NULL
);

CREATE TABLE Proveedores (
    id_proveedores VARCHAR (15) PRIMARY KEY
                                NOT NULL,
    nombre         CHAR (30),
    categoria      CHAR (15),
    ciudad         CHAR (20),
    direccion      CHAR (50),
    telefono       VARCHAR (15) 
);

