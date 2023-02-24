from config import AppFlask
from views.view import DatosScrapy,index,consultarToken

api = AppFlask().api
app = AppFlask().app

api.add_resource(DatosScrapy, "/price")
api.add_resource(consultarToken, "/token")
app.route('/', methods=["GET"])(index)


if __name__ == '__main__':
    app.run(host= app.config["HOST"],port=app.config["PORT"])

