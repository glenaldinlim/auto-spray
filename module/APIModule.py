from config import endpointUrl, pathVersion, headers
import urequests
import ujson

def getDataAPI(location):
    path = endpointUrl + pathVersion + location
    res = urequests.request("GET", path)
    return res.json()

def postDataAPI(location, req):
    path = endpointUrl + pathVersion + location
    body = ujson.dumps(req)
    res = urequests.post(path, headers=headers, data=body)
    return res.json()
