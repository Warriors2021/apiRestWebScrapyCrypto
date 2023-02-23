from config import AppFlask
from views.view import DatosScrapy,register

api = AppFlask.api
app = AppFlask.app

api.add_resource(DatosScrapy, "/price")
app.route('/register', methods=["GET","POST"])(register)


if __name__ == '__main__':
    app.run()


