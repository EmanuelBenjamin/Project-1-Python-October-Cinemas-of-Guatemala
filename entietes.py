class Movie():
    def __init__(self, id, title = None, url=None, classification=None):
        self.id= id
        self.title = title
        self.url = url
        self.classification = classification
        
        

    def to_JSON(self):
        return{
            'id':self.id,
            'title':self.title,
            'ulr':self.url,
            'classification':self.classification
        }

        

class User():
    def __init__(self, id, name = None, lastname=None, password=None, email=None, phone_number=None):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.password = password
        self.email = email
        self.phone_number = phone_number
        


class Ticket():
    def __init__(self, id, id_movie = None, seat_number = None, id_showtime = None):
        self.id = id
        self.id_movie = id_movie
        self.seat_number = seat_number
        self.id_showtime = id_showtime

class TicketInfo():
    def __init__(self, id_movie, title = None, url=None, clasification=None, create_all=None):
        self.id_movie = id_movie
        self.title = title
        self.url = url
        self.classification = clasification
    def to_JSON(self):
        return{
            'id': self.id_movie,
            'title':self.title,
            'url':self.url,
            'classification':self.classification,
        }
        
        
        
        