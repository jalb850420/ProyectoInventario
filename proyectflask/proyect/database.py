from os import error
import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('sesion12_g31.db')
        return con
    except :
        print ('error')

def sql_insert_producto(codigo, nombre, cantidad,precio):
    try:
        sql = f'insert into producto(id,nombre,existencia,precio) values ("{codigo}","{nombre}",{cantidad},{precio})'
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
    

def sql_select_productos():
    try:
        strsql = "select * from producto;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        productos = cursorObj.fetchall()
        return productos
    except Error as err:
        print(err)
	

def sql_edit_producto(id, codigo, nombre, cantidad):
    try:
        strsql = "update producto set id = '"+codigo+"', nombre = '"+nombre+"', existencia = "+cantidad+" where id = "+id+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
	

def sql_delete_producto(id):
    try:
        strsql = "delete from producto where id = "+id+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
	
