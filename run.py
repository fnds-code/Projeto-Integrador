from flask import Flask
from controllers.main_controller import main

app = Flask(__name__)

# Registra as rotas do Controller
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
