from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Proveedores(FlaskForm):
    id_proveedores = StringField('Codigo', validators=[DataRequired()])
    nombre = StringField('nombre', validators=[DataRequired()])
    categoria = StringField('categoria', validators=[DataRequired()])
    ciudad = StringField('ciudad', validators=[DataRequired()])
    direccion = StringField('direccion', validators=[DataRequired()])
    telefono = StringField('telefono', validators=[DataRequired()])
    enviar = SubmitField('Agregar Proveedores')


class Producto(FlaskForm):
    id_producto = StringField('Codigo', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    id_producto = StringField('Codigo', validators=[DataRequired()])
    marca = StringField('Cantidad', validators=[DataRequired()])
    descripcion = StringField('Descripcion', validators=[DataRequired()])
    categoria = StringField('Categoria', validators=[DataRequired()])
    costo = IntegerField('Costo', validators=[DataRequired()])
    precio = IntegerField('Precio', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    id_proveedores = StringField('id_proveedores', validators=[DataRequired()])
    enviar = SubmitField('Agregar Producto')


