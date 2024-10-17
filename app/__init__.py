from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mi_clave_secreta'  # Usa una clave secreta para la sesión
    
    from .routes import auth
    app.register_blueprint(auth)
    
    return app
