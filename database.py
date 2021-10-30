from os import error
import sqlite3
from sqlite3 import Error
from forms import EditProducto

from flask.templating import render_template

def sql_connection():
    try:
        con = sqlite3.connect('dbhotai.db')
        return con
    except :
        print ('error')

def sql_consulta_login(nombre, clave):
    try:
        strsql = "select * from Usuarios WHERE usuario = '"+nombre+"' and passw = '"+clave+"';" 
        con = sql_connection()
        cursorObj = con.cursor()
        valor = cursorObj.execute(strsql).fetchall()
        con.close()
        return valor
    except Error as err:
        print(err)
# USUARIO
def sql_nuevo_usuario(nombre, mail, perfil, usuario, passw, idtipousuario):
    try:
        strsql = f'insert into Usuarios(nombre, mail, perfil, usuario, passw, idTipo_Usuario) values ("{nombre}","{mail}","{perfil}","{usuario}","{passw}","{idtipousuario}")'
        con = sql_connection()
        cursorObj = con.cursor()
        valor = cursorObj.execute(strsql)
        con.commit()
        con.close()
        return valor
    except Error as err:
        print(err)


# TIPO DE USUARIO
def sql_insert_tipousuario(nom):
    try:
        sql = f'insert into Tipo_Usuario(nombreTU) values ("{nom}")'
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
    
def sql_edit_tipousuario(cod, nom):
    try:
        strsql = "update producto set id = '"+cod+"', nombre = '"+nom+" where id = "+cod+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)


# Usuario

def sql_insert_usuarios(id, nombre, mail, perfil, usuario, passw):
    try:
        sql = f'insert into Usuarios(id, nombre, mail, perfil, usuario, passw) values ("{id}","{nombre}",{mail},{perfil},{usuario},{passw})'
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
    

def sql_select_usuarios():
    try:
        strsql = "select * from Usuarios;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        usuarios = cursorObj.fetchall()
        return usuarios
    except Error as err:
        print(err)
	

def sql_edit_usuarios( nombre, mail, perfil, usuario, passw, idtipousuario, id):
    try:
        strsql = "update Usuarios set nombre = '"+nombre+"', mail = "+mail+", perfil = "+perfil+", usuario = "+usuario+", passw = "+passw+", idTipo_Usuario = "+idtipousuario+"  where id = "+id+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
	

def sql_delete_usuarios(id):
    try:
        strsql = "delete from Usuarios where id = "+id+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)

# PRODUCTO
def sql_select_productos():
    try:
        strsql = "select * from Productos;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        productos = cursorObj.fetchall()
        return productos
    except Error as err:
        print(err)

def sql_nuevo_producto(nombre, marca, descripcion, costo, cantidad, proveedor, categoria):
    try:
        sql = f'insert into Productos(nombre, marca, descripcion,  costo, cantidad, id_proveedores, idCategoria) values ("{nombre}","{marca}","{descripcion}","{costo}", "{cantidad}", "{proveedor}", "{categoria}")'
        con = sql_connection()
        cursorObj = con.cursor()
        prod=cursorObj.execute(sql)
        con.commit()
        con.close()
        return prod
    except Error as err:
        print(err)
#***************************************************
"""def sql_insert_producto(id_producto, nombre, marca, descripcion, categoria, costo, precio, cantidad):
    try:
        sql = f'insert into Productos(id_producto, nombre, marca, descripcion, categoria, costo, precio, cantidad) values ("{id_producto}","{nombre}",{marca},{descripcion},{categoria},{costo},{precio},{cantidad})'
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        con.commit()
        con.close()
    except Error as err:
        print(err)"""

def sql_edit_productos(id):
    try:
        strsql = "select * from Productos where id_producto ="+id+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        data = cursorObj.fetchall()
        return data[0]
    except Error as err:
        print(err)
	
def sql_actualizar_producto(idp, nomproducto, marcaproducto, descripproducto, costoproducto, precio, cantidad, idprov, idcategoria, id):
    try:
        strsql ="update Productos set id_producto = "+idp+", nombre = '"+nomproducto+"', marca = '"+marcaproducto+"', descripcion = '"+descripproducto+"', costo = '"+costoproducto+"', precio = '"+precio+"', cantidad = '"+cantidad+"', id_proveedores = "+idprov+", idCategoria = "+idcategoria+" where id_producto = "+id+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)


def sql_delete_productos(id):
    try:
        strsql = "delete from Productos where id_producto = "+id+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)

# PROVEEDORES
def sql_nuevo_proveedor(nombre, categoria, ciudad, direccion, telefono, idCategoria):
    try:
        strsql = f'insert into Proveedores(nombre, categoria, ciudad, direccion, telefono, idCategoria) values ("{nombre}","{categoria}","{ciudad}","{direccion}","{telefono}","{idCategoria}")'
        con = sql_connection()
        cursorObj = con.cursor()
        proveedor = cursorObj.execute(strsql)
        con.commit()
        con.close()
        return proveedor
    except Error as err:
        print(err)
    

def sql_select_proveedores():
    try:
        strsql = "select * from Proveedores;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        proveedores = cursorObj.fetchall()
        return proveedores
    except Error as err:
        print(err)
	

def sql_edit_proveedores(id_proveedores, nombre, categoria, ciudad, direccion, telefono):
    try:
        strsql = "update Proveedores set id_proveedores = '"+id_proveedores+"', nombre = '"+nombre+"', categoria = "+categoria+", ciudad = "+ciudad+", direccion = "+direccion+", telefono = "+telefono+" where id = "+id_proveedores+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
	

def sql_delete_proveedores(id_proveedores):
    try:
        strsql = "delete from Proveedores where id = "+id_proveedores+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
	
