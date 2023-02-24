from flask_restful import Resource
from models.modelMongoDB import conexion_mongo
from flask import jsonify, request
from flask import redirect, render_template,url_for, flash
from config import AppFlask
from forms.form import RegistrationForm, LoginForm
from models.modelMysql import User, Token
from flask_login import current_user,login_user,logout_user,login_required
from flask_jwt_extended import create_access_token
from marshmallow import Schema , fields


app = AppFlask().app
db = AppFlask().db

@app.route('/')
def index():

    return render_template("index.html", user = current_user)

@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:

        return redirect(url_for("index"))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        token = Token(token = create_access_token(identity=user.idusers))
        user.token = token
        db.session.add(token)
        db.session.commit()

        flash("Te has registrado exitosamente")

        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Nombre de usuario o contraseña inválidos.')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión exitosamente.', 'success')
    return redirect(url_for('index'))

class DatosScrapy(Resource):

    def get(self):

        conexion = conexion_mongo()

        token = request.headers.get('Authorization')

        token_existente = Token.query.filter_by(token=token).first()

        if token_existente:
            datos = conexion.ConsultarTodosLosDatos()
            return jsonify(datos)
        else:
            return "Token no válido", 401

        conexion.host.close()


class TokenSchema(Schema):
    token = fields.String()

class consultarToken(Resource):
    def get(self):
        if current_user.is_authenticated:
            tokens = Token.query.filter(Token.user.contains(current_user)).all()

            schema = TokenSchema(many=True)
            result = schema.dump(tokens)
            return jsonify({"Tokens": result})

        return redirect(url_for('login'))

