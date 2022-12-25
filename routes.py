from flask import Blueprint, jsonify, request
import json

#entities
from entietes import User
from entietes import Ticket

#models

from models import MovieModel
from models import UserModel
from models import LoginModel
from models import TicketModel


movies_main = Blueprint('movie_blueprint', __name__)
users_main = Blueprint('user_blueprint', __name__)
login_main =  Blueprint('login_blueprint', __name__ )
buy_ticket_main = Blueprint('buy_ticket', __name__)

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
        password = request.json['password']

        user=User("", "", "", password,"", "")
        affected_rows2 = LoginModel.verify_password(user)
        user=User("", "", "", "",email, "")
        affected_rows1 = LoginModel.verify_email(user)

        if affected_rows1 == 1 and affected_rows2 == 1:
            #auth = HTTPBasicAuth('email', 'password')
            #requests.post('https://postman-echo.com/basic-auth', auth=auth)
            #response = requests.get('https://postman-echo.com/basic-auth', auth=auth)
            #print(response.headers)
            return jsonify('exito')
        else:
            return jsonify({'message': "User not created"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@buy_ticket_main.route('/',methods=['POST'])

    
def buy_ticket():
    try:
        id_movie = int(request.json['id_movie'])
        seat_number = int(request.json['seat_number'])
        id_showtime = int(request.json['id_showtime'])
        ticket = Ticket("",id_movie, seat_number, id_showtime)
        affected_row = TicketModel.add_ticket(ticket)

    except Exception as ex:
        return jsonify({'message': str (ex)}), 500

