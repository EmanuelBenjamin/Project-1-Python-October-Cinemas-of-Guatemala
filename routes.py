from flask import Blueprint, jsonify, request
import json

#entities
from entietes import User

#models

from models import MovieModel
from models import UserModel


movies_main = Blueprint('movie_blueprint', __name__)
users_main = Blueprint('user_blueprint', __name__)
login_main =  Blueprint('login_blueprint', __name__ )

@movies_main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@users_main.route('/', methods = ['POST'])
def add_user():
    try:
        name = request.json['name']
        lastname = request.json['lastname']
        password = request.json['password']
        email = request.json['email']
        phone_number = int(request.json['phone_number'])
        user=User("", name, lastname, password, email, phone_number)
        affected_rows = UserModel.add_users(user)

        if affected_rows == 1:
            return jsonify('Registered user')
        else:
            return jsonify({'message': "usuario ya registrado"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@login_main.route('/', methods = ['GET', 'POST'])
def login():
    
    try:
        email = request.json['email']
        password = int(request.json['password'])
        user=User("", "", "", password,email, "")
        affected_rows = Login.login(user)
        if affected_rows == 1:
            return jsonify('Registered user')
        else:
            return jsonify({'message': "User not created"}), 500
    except Exception as ex:
        return jsonify({'message': "Invalid email or password"}), 
