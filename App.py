import os
from flask import Flask, render_template, request
from flask import g

from database import sql_insert_producto, sql_select_productos, sql_edit_productos, sql_delete_productos
from database import sql_select_proveedores, sql_insert_proveedores, sql_edit_proveedores, sql_delete_proveedores
from database import sql_select_usuarios, sql_insert_usuarios, sql_edit_usuarios, sql_delete_usuarios
from forms import Proveedores


App = Flask(__name__)
App.secret_key = os.urandom(24)


@App.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
   if  request.method == "GET": #Si la ruta es accedida a través del método GET entonces
	    form = Proveedores() #Crea un nuevo formulario de tipo producto
	    return render_template('nuevo.html', form=form) #redirecciona vista nuevo.html enviando la variable form
   if  request.method == "POST": #Si la ruta es accedida a través del método POST entonces
        id_proveedores = request.form["id_proveedores"] #asigna variable cod con valor enviado desde formulario  en la vista html
        nombre = request.form["nombre"] #asigna variable nom con valor enviado desde formulario en la vista html
        categoria = request.form["categoria"] #asigna vble cant con valor enviado desde formulario en la vista html
        ciudad = request.form["ciudad"] #asigna vble cant con valor enviado desde formulario en la vista html
        direccion = request.form["direccion"] #asigna vble cant con valor enviado desde formulario en la vista html
        telefono = request.form["telefono"] #asigna vble cant con valor enviado desde formulario en la vista html       sql_insert_proveedores(cod, nom, cant, precio) #llamado de la función para insertar el nuevo producto
        sql_insert_proveedores(id_proveedores, nombre, categoria, ciudad, direccion, telefono) #llamado de la función para insertar el nuevo producto
        return 'OK'

@App.route('/', methods=["GET","POST"])
def Home():
    return render_template('home.html')

@App.route('/Inicio', methods=["GET","POST"])
def Inicio():
    g.nombre = request.form.get("nombre")
    return render_template('inicio.html', nombre=g.nombre)

@App.route('/Usuarios', methods=["GET", "POST"])
def Usuario():
    return render_template('usuario.html')

@App.route('/Productos', methods=["GET", "POST"])
def Productos():
    return render_template('productos.html')

@App.route('/Proveedores', methods=["GET", "POST"])
def Proveedores():
    return render_template('proveedores.html')

@App.errorhandler(404)
def not_found(error):
        return "La página no existe"

if __name__ == '__main__':
    App.run(debug = True)
