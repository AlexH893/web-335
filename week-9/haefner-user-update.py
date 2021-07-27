#
############################################
# Title:  haefner-user-update.py
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

# Updating user email 
db.users.update_one(
    {"employee_id": "0000001"},
    {
        "$set": {
            "email": "ahaefner@my365.bellevue.edu"
        }
    }
)


# Printing result
pprint.pprint(db.users.find_one({"employee_id": "0000001"}))