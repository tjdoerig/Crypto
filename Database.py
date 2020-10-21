'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print(myclient)

dblist = myclient.list_database_names()
path = myclient.address

print(dblist)

#Check if database exists
if "mydatabase" in dblist:
  print("The database exists.")
else:
  mydb = myclient["mydatabase"]
  mycol = mydb["customers"]

  mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
  ]

  x = mycol.insert_many(mylist)

  #print list of the _id values of the inserted documents:
  #print(x.inserted_ids)

  x = mycol.find_one()

  print(x)

'''

# import the MongoClient class
from pymongo import MongoClient, errors

# default port is 27017
DOMAIN = 'localhost:'
PORT = 27017

# use a try-except indentation to catch MongoClient() errors
try:
    # try to instantiate a client instance
    client = MongoClient(
        host = [ str(DOMAIN) + str(PORT) ],
        serverSelectionTimeoutMS = 3000 # 3 second timeout
    )

    # print the version of MongoDB server if connection successful
    print ("server version:", client.server_info()["version"])
    
except errors.ServerSelectionTimeoutError as err:
    # set the client instance to 'None' if exception
    client = None

    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)


if client != None:

    # the list_database_names() method returns a list of strings
    database_names = client.list_database_names()

    print ("database_names() TYPE:", type(database_names))
    print ("The client's list_database_names() method returned", len(database_names), "database names.")

    # iterate over the list of database names
    for db_num, db in enumerate(database_names):

        # print the database name
        print ("\nGetting collections for database:", db, "--", db_num)
        
        # use the list_collection_names() method to return collection names
        collection_names = client[db].list_collection_names()
        print ("list_collection_names() TYPE:", type(database_names))
        print ("The MongoDB database returned", len(collection_names), "collections.")

        # iterate over the list of collection names
        for col_num, col in enumerate(collection_names):
            print (col, "--", col_num)
            
else:
    print ("The domain and port parameters passed to client's host is invalid")

