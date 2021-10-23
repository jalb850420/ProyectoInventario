import os
from flask import Flask, request, render_template, redirect, url_for, flash


from database import sql_insert_tipousuario, sql_select_productos, sql_delete_productos , sql_edit_productos, sql_actualizar_producto
from forms import  TipoUsuario,Producto, EditProducto
app = Flask(__name__)
#app.secret_key = os.urandom(24)
app.secret_key ='mysecretkey'



@app.route('/', methods=['GET', 'POST']) 
def hola(): 
  return "Hola mundo"

@app.route('/productos', methods=['GET', 'POST']) 
def productos(): 
  form=Producto()
  productos = sql_select_productos()
  return render_template('productos.html', productos = productos, form = form)
 
@app.route('/edit/<id>', methods=['GET'])
def editar_producto(id):
   form=EditProducto()
   data = sql_edit_productos(id)
   return render_template('editProducto.html',data = data, form = form)
   #return "OK"
 #   id = request.args.get('id') #captura de la variable id enviada a través de la URL
 #   codigo = request.args.get('codigo') #captura de la vble código enviada a través de la URL
 #   nombre = request.args.get('nombre') #captura de la vble nombre enviada a través de la URL
 #   cantidad = request.args.get('cantidad') #captura de la vble cantidad enviada a través de la URL
 #   sql_edit_producto(id, codigo, nombre, cantidad) #llamado de la función de edición de la base de datos
 #   return "OK"


@app.route('/actualizar/<id>', methods=['POST'])
def actualizar_producto(id):
   if  request.method == "POST": #Si la ruta es accedida a través del método POST entonces
      idp = request.form["IdProducto"] #captura de la variable id enviada a través de la URL
      nomproducto = request.form["NombreProducto"] #captura de la vble código enviada a través de la URL
      marcaproducto = request.form["MarcaProducto"] #captura de la vble nombre enviada a través de la URL
      descripproducto = request.form["DescripProducto"] #captura de la vble cantidad enviada a través de la URL
      costoproducto = request.form["CostoProducto"] #captura de la variable id enviada a través de la URL
      precio = request.form["Precio"] #captura de la vble código enviada a través de la URL
      cantidad = request.form["Cantidad"] #captura de la vble nombre enviada a través de la URL
      idprov = request.form["IdProv"] #captura de la vble cantidad enviada a través de la URL
      idcategoria = request.form["IdCategoria"] #captura de la vble cantidad enviada a través de la URL
      sql_actualizar_producto(idp, nomproducto, marcaproducto, descripproducto, costoproducto, precio, cantidad, idprov, idcategoria, id) #llamado de la función de edición de la base de datos
      return redirect(url_for('productos'))

@app.route('/delete/<id>')
def borrar_producto(id):
   sql_delete_productos(id) #llamado a la función de borrado de la base de datos
   return redirect(url_for('productos'))



# TIPO DE USUARIO

@app.route('/nuevo_Tipo_Usuario', methods=['GET', 'POST'])
def nuevotipousuario():
   if  request.method == "GET": #Si la ruta es accedida a través del método GET entonces
	    form = TipoUsuario() #Crea un nuevo formulario de tipo producto
	    return render_template('nuevo_Tipo_Usuario.html', form=form) #redirecciona vista nuevo.html enviando la variable form
   if  request.method == "POST": #Si la ruta es accedida a través del método POST entonces
        cod = request.form["codigo"] #asigna variable cod con valor enviado desde formulario  en la vista html
        nom = request.form["nombre"] #asigna variable nom con valor enviado desde formulario en la vista html
        sql_insert_tipousuario(cod, nom) #llamado de la función para insertar el nuevo producto
        flash('Dato almacenado con exito!')
        return redirect(url_for('nuevotipousuario'))



