from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Proveedores(FlaskForm):
    id_proveedores = StringField('id_proveedores', validators=[DataRequired()])
    nombre = StringField('nombre', validators=[DataRequired()])
    categoria = IntegerField('categoria', validators=[DataRequired()])
    ciudad = IntegerField('ciudad', validators=[DataRequired()])
    direccion = IntegerField('direccion', validators=[DataRequired()])
    telefono = IntegerField('telefono', validators=[DataRequired()])
    enviar = SubmitField('Agregar Proveedores')



