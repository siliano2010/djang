from django.db import models
import pyrebase

firebaseconfig={
"apiKey": "AIzaSyAMGxSJ0Tn5jE10rZ0zA2dVyrbauE63qdU",
"authDomain": "house2021-24b35.firebaseapp.com",
"databaseURL": "https://house2021-24b35-default-rtdb.firebaseio.com",
"projectId": "house2021-24b35",
"storageBucket": "house2021-24b35.appspot.com",
"messagingSenderId": "286984037551",
"appId": "1:286984037551:web:154aaa1089c2e4bde9a05a",
"measurementId": "G-ESL2Q4YT1N"
}
firebase = pyrebase.initialize_app(firebaseconfig)
auth=firebase.auth()
def authlogin(email,senha):
    try:
        o=auth.sign_in_with_email_and_password(email,senha)
        
        return o
    except Exception as err:
        
        return False





    

