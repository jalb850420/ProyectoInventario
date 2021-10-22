from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Proveedores(FlaskForm):
    codigo = StringField('Codigo', validators=[DataRequired()])
    nombre = StringField('nombre', validators=[DataRequired()])
    categoria = IntegerField('categoria', validators=[DataRequired()])
    ciudad = IntegerField('ciudad', validators=[DataRequired()])
    direccion = IntegerField('direccion', validators=[DataRequired()])
    telefono = IntegerField('telefono', validators=[DataRequired()])
    enviar = SubmitField('Agregar Proveedores')

class Producto(FlaskForm):
    id_producto = StringField('Codigo', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    marca = IntegerField('Cantidad', validators=[DataRequired()])
    descripcion = IntegerField('Descripcion', validators=[DataRequired()])
    categoria = IntegerField('Categoria', validators=[DataRequired()])
    costo = IntegerField('Costo', validators=[DataRequired()])
    precio = IntegerField('Precio', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    id_proveedores = IntegerField('id_proveedores', validators=[DataRequired()])
    enviar = SubmitField('Agregar Producto')


