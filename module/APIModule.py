from config import endpointUrl, pathVersion, headers
import urequests as requests
import ujson

def getData(location):
    path = endpointUrl + pathVersion + location
    res = requests.get(path, headers=headers)
    return res.json()

def postData(location, req):
    path = endpointUrl + pathVersion + location
    body = ujson.dumps(req)
    res = requests.post(path, headers=headers, data=body)
    return res.json()
    
