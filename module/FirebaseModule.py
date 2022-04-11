import ufirebase as firebase
from config import firebaseUrl, firebasePathVersion

firebase.setURL(firebaseUrl)

def getData(location):
    path = firebasePathVersion + location
    firebase.get(path, "value")
    
    return firebase.value

def storeData(location, data):
    path = firebasePathVersion + location
    firebase.addto(path, data)
    
    return "Sucessfull store data to {0} with value {1}".format(path, data)
    
def putData(location, data):
    path = firebasePathVersion + location
    firebase.put(path, data)
    
    return "Sucessfull update data to {0} with value {1}".format(path, data)
    
def deleteData(location):
    path = firebasePathVersion + location
    firebase.delete(path)
