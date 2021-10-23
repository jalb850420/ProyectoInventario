from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Producto(FlaskForm):
    codigo = StringField('Codigo', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    precio = IntegerField('Precio', validators=[DataRequired()])
    enviar = SubmitField('Agregar Producto')
