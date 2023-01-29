from djongo import models
from pymongo import MongoClient
class Authen:
    def __init__(self):
        try:
            self.conn = MongoClient("mongodb+srv://prash:2808@authenticate.1eugga8.mongodb.net/?retryWrites=true&w=majority")
            print("Connected successfully!!!")
        except:  
            print("Could not connect to MongoDB")
        # database
        self.db = self.conn.Authenticate
        # Created or Switched to collection names: my_gfg_collection
        self.collection = self.db.users
        self.collection2 = self.db.reviews
    def insert(self,name,pas): 
        r1 = {"name":name,"password":pas }
        # Insert Data
        rec_id1 = self.collection.insert_one(r1)
            
    def isvalid(self,name,pas):
        cursor = self.collection.find()
        for record in cursor:
            if record['name']==name and record['password']==pas:
                return True   
        return False
    def addreview(self,fname,review):
        r={"fname":fname,"review":review}
        self.collection2.insert_one(r)
    def fetchreview(self):
        reviews=self.collection2.find()
        return reviews
        
        
    
            
