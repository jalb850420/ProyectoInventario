from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class TipoUsuario(FlaskForm):
    codigo = StringField('Tipo de Usuario', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    enviar = SubmitField('Agregar Tipo de Usuario')

class Producto(FlaskForm):
    id = StringField('Id Producto', validators=[DataRequired("Tienes que introducir el dato")])
    enviar = SubmitField('Ver Producto')

class EditProducto(FlaskForm):
    IdProducto = StringField('Id Producto', validators=[DataRequired()])
    NombreProducto = StringField('Nombre', validators=[DataRequired()])
    MarcaProducto = StringField('Marca', validators=[DataRequired()])
    DescripProducto = StringField('Descripcion', validators=[DataRequired()])
    CostoProducto = StringField('Costo', validators=[DataRequired()])
    Precio = StringField('Precio', validators=[DataRequired()])
    Cantidad = StringField('Cantidad', validators=[DataRequired()])
    IdProv = StringField('Id Proveedor', validators=[DataRequired()])
    IdCategoria = StringField('Id Catedoria', validators=[DataRequired()])
    enviar = SubmitField('Actualizar')