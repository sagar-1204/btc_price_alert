from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, JWTManager
from models import User, db

auth = Blueprint('auth', __name__)

# Initialize JWTManager somewhere in your main application file, not in the Blueprint.
# jwt = JWTManager(app)

@auth.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Validate the input
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Missing username, email, or password'}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 409

    hashed_password = generate_password_hash(password, method='sha256')

    new_user = User(
        username=username,
        email=email,
        password_hash=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registered successfully'}), 201

@auth.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Missing email or password'}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Bad username or password'}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200
