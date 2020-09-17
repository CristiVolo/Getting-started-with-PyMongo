#  8-66-Inserting getting started
# -------------------------------
# PyMongoInstallation
# ---------------------------

#  8-67-Inserting documents
# ---------------------------
# import pymongo
# from pymongo import MongoClient
# myClient = MongoClient()
# db = myClient.mydb
# users = db.users
# user1 = {"username": "nick", "password": "myverysecurepassword", "favorite_number": 445, "hobbies": ["python",
#         "games", "pizza"]}
# user_id = users.insert_one(user1).inserted_id
# user_id
# # user1 is being inserted again.
# ---------------------------

#  8-68-Bulk inserts
# ---------------------------
# users = [{"username": "third", "password": "12345"}, {"username": "red", "password": "blue"}]
# Users = db.users
# inserted = Users.insert_many(users)
# inserted.inserted_ids
# ---------------------------

#  8-69-Counting documents
# ---------------------------
# Users.find().count()
# Users.find({"favorite_number": 445}).count()
# ---------------------------

#  8-70-Multiple find conditions
# ---------------------------
# Users.find({"favorite_number": 445, "hobbies": ["python", "gaming", "pizza"]}).count()
# ---------------------------

#  8-71-Datetime and keywords
# ---------------------------
# import datetime
# current_date = datetime.datetime.now()
# current_date
# datetime.datetime(2020, 9, 17, 19, 45, 47, 171283)
# old_date = datetime.datetime(2009, 8, 11)
# uid = Users.insert({"username": "f", })
# <stdin>:1: DeprecationWarning: insert is deprecated. Use insert_one or insert_many instead.
#
# uid = Users.insert({"username": "f", "date": current_date})
# uid = Users.insert_one({"username": "f", "date": current_date})
# Users.find("date": {"$gt": old_date}).count()
#  File "<stdin>", line 1
#    Users.find("date": {"$gt": old_date}).count()
#
# SyntaxError: invalid syntax
# Users.find({"date": {"$gt": old_date}}).count()
#
# Users.find({"date": {"$lte": old_date}}).count()
#
# Users.find({"date": {"$exists": True}}).count()
#
# Users.find({"username": {"$ne": yetanother}}).count()
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# NameError: name 'yetanother' is not defined
# Users.find({"username": {"$ne": "yetanother"}}).count()
# ---------------------------

#  8-72-Indexes
# ---------------------------
# db.users.create_index()
# db.users.create_index([("username", pymongo.ASCENDING)], unique=True)
# Users.find({"username": "nick"})
# ---------------------------
