# Importar los módulos necesarios
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

# Definir la clase para el formulario de registro
class RegistrationForm(FlaskForm):
    # Crear un campo para el nombre, requerido
    name = StringField('Nombre', validators=[DataRequired()])
    # Crear un campo para el correo electrónico, requerido
    email = StringField('Correo electrónico', validators=[DataRequired()])
    # Crear un campo para la contraseña, requerido
    password = PasswordField('Contraseña', validators=[DataRequired()])
    # Crear un campo para confirmar la contraseña, requerido
    confirm_password = PasswordField('Confirmar contraseña', validators=[DataRequired()])
    # Crear un botón de envío con el texto "Registrarse"
    submit = SubmitField('Registrarse')

# Definir la clase para el formulario de inicio de sesión
class LoginForm(FlaskForm):
    # Crear un campo para el nombre, requerido
    name = StringField('Nombre', validators=[DataRequired()])
    # Crear un campo para la contraseña, requerido
    password = PasswordField('Contraseña', validators=[DataRequired()])
    # Crear un botón de envío con el texto "Ingresar"
    submit = SubmitField('Ingresar')
