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
    def __init__(self, id, name = None, lastname=None, password=None, phone_number=None,):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.password = password
        #self.email = email
        self.phone_number = phone_number
        

class token():
    def __init__(self, id_token, key_code= None, user_id=None, user=None, create_all=None):
        self.id_token = id_token
        self.key_code = key_code
        self.user_id = user_id
        self.user = user
        self.create_all = create_all
