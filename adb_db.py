#Importing TinyDB and Query from the tinydb module
from tinydb import TinyDB, Query

#Initializing database as the database so we can work with it
database = TinyDB('adb_db.json')

#These lines inserted mine and Larry's named, numbers, and addresses into the database.
#database.insert({"name": "Lilith Ashbury", "phone number": "3607912409", "address": "108 20th Ave SW"})
#database.insert({"name": "Larry Lecrone", "phone number": "2063139830", "address": "108 20th Ave SW"})

#iterates through the database and prints out each piece of it.
#for item in database.search({})
#   print(item)

infoquery = Query()                                                     #Initialize a query
FullUserInfo = database.get(infoquery['name'] == 'Larry Lecrone')       #Sets FullUserInfo to the document with the name "Larry Lecrone"
name = FullUserInfo.get('name')                                         #
address = FullUserInfo.get('address')                                   #Gets the name, addy, and phone number and assigns them to a variable of the same name
phone_number = FullUserInfo.get('phone number')                         #
print(f"{name}: {phone_number} - {address}")                            #Creates a pretty string with the name, addy, and phone number

#Testing = database.get(TestQuery['name'] == "Larry Lecrone")
#print(Testing.get('name'))
#print(Testing.get('phone number'))
#print(Testing.get('address'))

#DBSize = database.all()[-1].doc_id
#print("The database size is:", DBSize)
#for item in range(DBSize):
#    print("Printing out objects from the database record: ", item+1)
    #'''
   # Get's a documents info based on index number. [item}
    #>>> FullUserInfo = (database.all()[item])
    #'''

    #'''
   # FullUserInfo = database.search(infoquery['name'] == 'Larry Lecrone')
   # print(FullUserInfo.get('name'))
   # print(FullUserInfo.get('phone number'))
   # print(FullUserInfo.get('address'))
  #  '''