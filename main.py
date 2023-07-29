from class_firebase_database import FirebaseDB
from firebase_admin import  db

path ="credenciales de tu base de datos.json"
url ="url de tu base de datos en firebase"

fb_db = FirebaseDB(path,url)


"""

# Write data to the database
data_to_write = {
'name': 'jj',
'age': 27,
'email': 'jj@gmail.com'
}
fb_db.write_record('/users/jj', data_to_write)

# Read data from the database
result = fb_db.read_record('/users/toni')
print("Read Data:", result)

# Update data in the database
data_to_update = {
'age': 31
}
fb_db.update_record('/users/toni', data_to_update)

# Delete data from the database
fb_db.delete_record('/users/john_doe')

# Delete data from the database
fb_db.delete_record('/users/toni')

# to save a record with an unique id
ref = db.reference('users')
new_email_ref = ref.push()
new_email_ref.set({
    'name': 'Juan',
    'email': 'Juan@hotmail.com'
})

"""

