import firebase_admin
from firebase_admin import credentials, db

class FirebaseDB:
    def __init__(self, credential_path, database_url):
        # Initialize Firebase with your service account credentials
        cred = credentials.Certificate(credential_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': database_url
        })

    def write_record(self, path, data):
        # Write data to the specified path in the Realtime Database
        ref = db.reference(path)
        ref.set(data)

    def read_record(self, path):
        # Read data from the specified path in the Realtime Database
        ref = db.reference(path)
        return ref.get()

    def update_record(self, path, data):
        # Update data at the specified path in the Realtime Database
        ref = db.reference(path)
        ref.update(data)

    def delete_record(self, path):
        # Delete data at the specified path in the Realtime Database
        ref = db.reference(path)
        ref.delete()