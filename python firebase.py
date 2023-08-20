import pyrebase
import random

#example url : https://parkingggg-a87c54-default-rtdb.firebaseio.com

config = {
    "apiKey": "WxPxKcNRcpVcvcvjcedbToGrHb0k6oqkC9K3rC9Gbw7g",
    "authDomain": "parkingggg-a87c54.firebaseapp.com",
    "databaseURL": "https://parking-a87c54-default-rtdb.firebaseio.com/",
    "storageBucket": "parkingggg-a87c54.appspot.com"
}



firebase = pyrebase.initialize_app(config)

db = firebase.database()

while True:
    data = {
        "SLOT1": random.randrange(1, 10),
        "SLOT2": random.randrange(10, 50),
        "SLOT3": random.randrange(10, 50),
        "SLOT4": random.randrange(10, 50),
    }

    print(data)

    db.update(data)
