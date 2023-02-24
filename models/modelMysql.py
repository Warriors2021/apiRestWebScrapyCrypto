# Importar la clase AppFlask desde el módulo config, que es el archivo de configuración de la aplicación Flask
# Importar la clase UserMixin desde el módulo flask_login para permitir la autenticación de usuarios
# Importar las funciones check_password_hash y generate_password_hash desde el módulo werkzeug.security para generar y verificar contraseñas seguras
from config import AppFlask
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

# Crear una instancia de la base de datos de la aplicación Flask
# Crear una instancia del administrador de login de la aplicación Flask
db = AppFlask().db
login_manager = AppFlask().loginManager

# Definir el modelo de usuario para la base de datos
class User(UserMixin, db.Model):
    # Definir el nombre de la tabla en la base de datos para este modelo
    __tablename__ = "users"
    # Definir los campos de la tabla de la base de datos
    idusers = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    token_id = db.Column(db.Integer, db.ForeignKey('tokens.id'))
    token = db.relationship('Token', backref='user', uselist=False)

    # Definir la representación en string de este modelo
    def __repr__(self):
        return '<User %r>' % self.name

    # Definir una función para establecer la contraseña de este usuario
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Definir una función para verificar si la contraseña proporcionada coincide con la contraseña de este usuario
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Definir una función para obtener el identificador único de este usuario
    def get_id(self):
        return str(self.idusers)

# Definir una función para cargar un usuario a partir de su identificador único
# Esta función se utiliza para la autenticación de usuarios en Flask-Login
@login_manager.user_loader
def load_user(idusers):
    return User.query.get(int(idusers))

# Definir el modelo de token para la base de datos
class Token(db.Model):
    # Definir el nombre de la tabla en la base de datos para este modelo
    __tablename__ = 'tokens'
    # Definir los campos de la tabla de la base de datos
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable=False)

