from pymongo import MongoClient
import sys

#Command line arguments
db_name = sys.argv[1]
role_name = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]

uri = "mongodb://#########################:27017/?authSource=admin"
demo_client = MongoClient(uri) 
demo_db = demo_client[db_name]

#Creating Role for DB
demo_db.command("createRole",role_name , privileges=[
{ "resource": { "db": db_name, "collection": "" }, "actions": [ "find", "listIndexes", "listCollections", "dbStats", "collStats", "createCollection", "createIndex", "insert", "update", "remove" ] }],roles=[])

#Creating User for DB
demo_db.add_user( username, password , roles=[{'role': role_name ,'db': db_name }])




