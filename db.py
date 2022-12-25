import psycopg2
from psycopg2 import DatabaseError
from decouple import config

from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey  

Base = declarative_base()
def get_conection():
    try:
        return psycopg2.connect(
            host = config('PGSQL_HOST'),
            user = config('PGSQL_USER'),
            password = config ('PGSQL_PASSWORD'),
            database = config('PGSQL_DATABASE')
         )
    except DatabaseError as ex:
        raise ex

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key = True)
    name = Column(String, nullable = False)
    lastname = Column(String, nullable = False)
    password = Column(String, nullable = False )
    email=Column(String, nullable = True)
    phone_number = Column(Integer,nullable = False )
    tokens = relationship('token', back_populates='user')
   

    
class token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key = True)
    key_code = Column(String, nullable = False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users', back_populates = 'tokens')
    

class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    url = Column(String, nullable = False)
    classification = Column(String, nullable = False)
    showtimes = relationship('Showtime', back_populates = 'movie')
    ticket = relationship('Ticket', back_populates = 'movie')

class Showtime(Base):
    __tablename__ = 'showtimes'

    id = Column(Integer, primary_key = True)
    date = Column(String, nullable = False)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    movie = relationship('Movie', back_populates = 'showtimes')


class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key = True)
    id_movie = Column(Integer, nullable = False)
    seat_number = Column(Integer, nullable = False)
    id_showtime = Column(Integer, nullable = False)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    movie = relationship('Movie', back_populates = 'ticket')

    

engine = create_engine('postgresql://postgres:12345@localhost/database')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



    
