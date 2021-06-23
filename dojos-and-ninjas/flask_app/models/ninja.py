from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.dojo import Dojo



class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []
        for ninja in results: 
            ninjas.append(cls(ninja))
        return ninjas



    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM ninjas WHERE ninjas.id = %(id)s'
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(results)
        return cls(results[0])    

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id, created_at, updated_at ) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW() )";
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )



    @classmethod
    def get_by_dojoid(cls):
        query = "SELECT * FROM ninjas WHERE ninjas.dojo_id = %(dojo_id)s "
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []
        for ninja in results: 
            ninjas.append(cls(ninja))
        return ninjas

# ------------------------------------------------------------


    # @classmethod
    # def get_dojo_with_ninjas( cls , data ):
    #     query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(id)s;"
    #     results = connectToMySQL('dojos_and_ninjas').query_db( query , data )
    #     # groups will be a list of music group objects from our raw data
    #     dojo = cls( results[0] )
    #     for row_from_db in results:
            
    #         ninja_data = {
    #             "id" : row_from_db["ninja.id"],
    #             "first_name" : row_from_db["ninjas.first_name"],
    #             "last_name" : row_from_db["ninjas.last_name"],
    #             "age" : row_from_db["age"],
    #             "created_at" : row_from_db["ninjas.created_at"],
    #             "updated_at" : row_from_db["ninjas.updated_at"]
    #         }
    #         dojo.ninjas.append = ninja.Ninja( ninja_data )
    #     return dojo