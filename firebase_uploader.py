import pyrebase


class FilestoCloud:

    def __init__(self,predicted_text='None'):
        self.predicted_text = predicted_text
        
        self.config = {
            "apiKey": "AIzaSyBBKLXbucDNEuSQbo9_FuCrfKzvCjKCCzo",
            "authDomain": "airdraw1.firebaseapp.com",
            "databaseURL": "",
            "projectId": "airdraw1",
            "storageBucket": "airdraw1.appspot.com",
            "serviceAccount": "serviceAccountKey.json"
        }

    def upload_file(self):
        firebase_storage = pyrebase.initialize_app(self.config)
        storage = firebase_storage.storage()

        textobject = open("predicted_text.txt","w")
        textobject.writelines(self.predicted_text)
        textobject.close()
        storage.child("predicted_text.txt").put("predicted_text.txt")
        print("File uploaded")