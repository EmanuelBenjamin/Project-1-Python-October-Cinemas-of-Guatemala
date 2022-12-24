from flask import jsonify
from db import get_conection
from entietes import Movie
import requests

class MovieModel():
    @classmethod
    def get_movies(self):
        try:
            connection = get_conection()
            movies=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, url, classification FROM movies ORDER BY title ASC")
                resulset = cursor.fetchall()

                for row in resulset:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_JSON())
            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)
class UserModel():
    @classmethod
    def add_users(self, users):
        try:
            connection = get_conection()
            with connection.cursor() as cursor:
                existing_user = """SELECT name, lastname, password, email, phone_number FROM users 
                            WHERE email = '{}' """.format(users.email)
                cursor.execute(existing_user)
                row = cursor.fetchone()
                if row == None:
                    cursor.execute("""INSERT INTO users (name, lastname, password, email, phone_number) 
                            VALUES (%s, %s, %s, %s, %s)""".format(users.email),(users.name, users.lastname, users.password, users.email, users.phone_number))
                    affected_row = cursor.rowcount
                    connection.commit()
                else:
                    return None
            connection.close()
            return affected_row
        except Exception as ex:
            raise Exception(ex)
class LoginModel():
    @classmethod
    def verify_email(self, users):
        try:
            connection = get_conection()
            with connection.cursor() as cursor:
                existing_user = """SELECT name, lastname, password, email, phone_number FROM users 
                            WHERE email = '{}'""".format(users.email)
                cursor.execute(existing_user)
                row = cursor.fetchone()
                if row != None:
                    affected_row1 = 1
                else:
                    return None
            connection.close()
            return affected_row1
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def verify_password(self, users):
        try:
            connection = get_conection()
            with connection.cursor() as cursor:
                existing_user = """SELECT name, lastname, password, email, phone_number FROM users 
                            WHERE password = '{}'""".format(users.password)
                cursor.execute(existing_user)
                row = cursor.fetchone()
                if row != None:
                    affected_row2 = 1
                else:
                    return None
            connection.close()
            return affected_row2
        except Exception as ex:
            raise Exception(ex)