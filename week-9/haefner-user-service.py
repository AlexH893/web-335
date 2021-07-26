#
############################################
# Title:  haefner-user-service.py
# Author: Alex Haefner
# Date:   24 Jul 2021
# Description: Python script
############################################
#

# Import statements
from pymongo import MongoClient
import pprint
import datetime

# Connecting to MongoDB
client = MongoClient('localhost', 27017)
# Using web335 DB
db = client.web335


# Creating user document
user = {
    "first_name": "Person",
    "last_name": "Python",
    "email": "python@me.com",
    "employee_id": "0000001",
    "date_created": datetime.datetime.utcnow()
}

# Inserting user document
user_id = db.users.insert_one(user).inserted_id

# Printing user id
print(user_id)

# Querying collection and printing document
pprint.pprint(db.users.find_one({"employee_id": "0000001"}))