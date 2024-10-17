from flask import Blueprint, request, jsonify, session

auth = Blueprint('auth', __name__) 

# simular bases de datos

users = {
    "usuario1": "password1",
    "usuario2": "password2"
}

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Corrección aquí
    
    username = data.get('username')
    password = data.get('password')
    
    # Validación simple
    if username in users and users[username] == password:
        # Crear la sesión del usuario
        session['user'] = username
        return jsonify({"message": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"message": "Usuario o contraseña incorrectos"}), 401


@auth.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return jsonify({"message": "Sesión cerrada"}), 200

    

