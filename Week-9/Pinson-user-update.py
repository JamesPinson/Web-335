# ========================================
# Title: Exercise 9.3
# Author: James Pinson
# Date: May 12th 2021
# Description: This shows us how to use python to update a document.
# ========================================

# This imports pymongo, pprint, and datetime.
from pymongo import MongoClient
import pprint
import datetime

# This connects to the local MongoDB instance
client = MongoClient('localhost', 27017)
db = client.web335

# This updates our user information.
db.users.update_one(
    {"employee_id": "8901928"},
    {
        "$set": {
            "email": "evanslacey@mail.com"
        }
    }
)

# This prints out our users information based on the searched email.
pprint.pprint(db.users.find_one({"email": "evanslacey@mail.com"}))
