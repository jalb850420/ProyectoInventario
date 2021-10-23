import os
from flask import Flask, request, render_template


from database import sql_insert_tipousuario, sql_select_productos#, sql_edit_producto, sql_delete_producto
from forms import  TipoUsuario,Producto
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/productos', methods=['GET', 'POST']) 
def productos(): 
  form=Producto()
  productos = sql_select_productos()
  return render_template('productos.html', productos = productos, form = form)
 

@app.route('/nuevo_Tipo_Usuario', methods=['GET', 'POST'])
def nuevotipousuario():
   if  request.method == "GET": #Si la ruta es accedida a través del método GET entonces
	    form = TipoUsuario() #Crea un nuevo formulario de tipo producto
	    return render_template('nuevo_Tipo_Usuario.html', form=form) #redirecciona vista nuevo.html enviando la variable form
   if  request.method == "POST": #Si la ruta es accedida a través del método POST entonces
        cod = request.form["codigo"] #asigna variable cod con valor enviado desde formulario  en la vista html
        nom = request.form["nombre"] #asigna variable nom con valor enviado desde formulario en la vista html
        sql_insert_tipousuario(cod, nom) #llamado de la función para insertar el nuevo producto
        return 'OK'

@app.route('/edit', methods=['GET'])
def editar_producto():
    id = request.args.get('id') #captura de la variable id enviada a través de la URL
    codigo = request.args.get('codigo') #captura de la vble código enviada a través de la URL
    nombre = request.args.get('nombre') #captura de la vble nombre enviada a través de la URL
    cantidad = request.args.get('cantidad') #captura de la vble cantidad enviada a través de la URL
 #   sql_edit_producto(id, codigo, nombre, cantidad) #llamado de la función de edición de la base de datos
    return "OK"

@app.route('/delete', methods=['GET'])
def borrar_producto():
	id = request.args.get('id') #captura de la variable id enviada a través de la URL
#sql_delete_producto(id) #llamado a la función de borrado de la base de datos
	return "OK"

