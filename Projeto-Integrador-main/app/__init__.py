
from flask import Flask


def criar_app():
    app = Flask(__name__)

    from app.controllers.pratos_controller import pratos_bp

    app.register_blueprint(pratos_bp)

    @app.route("/api")
    def inicio_api():
        return {
            "projeto": "Sabor & Clic",
            "mensagem": "API funcionando!",
            "versao": "Parte 1"
        }

    return app