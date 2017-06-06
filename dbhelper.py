from bson.objectid import ObjectId
import pymongo

DATABASE = "waitercaller"

class DBHelper:

    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client[DATABASE]

    def get_user(self, email):
        return self.db.users.find_one({"email":email})

    def add_user(self, email, salt, hashed):
        self.db.users.insert({"email": email, "salt": salt, "hashed", hashed})

    def add_table(self, number, owner):
        new_id = self.db.tables.insert({"number": number, "owner": owner})
        return new_id

    def update_table(self, _id, url):
        self.db.tables.update({"_id": _id}, {"$set": {"url": url}})

    def get_tables(self, owner_id):
        return list(self.db.tables.find_one({"owner": owner_id}))

    def get_table(self, table_id):
        return self.db.tables.find_one("_id": ObjectId(table_id))

    def delete_table(self, table_id):
        self.db.tables.remove({"_id": ObjectId(table_id)})