# ========================================
# Title: Exercise 9.2
# Author: James Pinson
# Date: May 12th 2021
# Description: This shows us how to use python to create documents and query them.
# ========================================

# This imports pymongo, pprint, and datetime.
import pymongo
import pprint
import datetime

# This connects to the local MongoDB instance
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print(client)

# This creates a new user document.
client = MongoClient('localhost', 27017)
db = client.web335
user = {
    "first_name": "Lacey",
    "last_name": "Evans",
    "email": "laceyevans@mail.com",
    "employee_id": "8901928",
    "date_created": datetime.datetime.utcnow()
}

# This inserts the new user document into our database.
user_id = db.users.insert_one(user).inserted_id

# This outputs the user_id
print(user_id)

# This prints the document using the find_one query.
pprint.pprint(db.users.find_one({"employee_id": "8901928"}))
