from filtrar import readRequest, updateCookie
import requests

req = readRequest()

#Primer request
cookie = requests.request("GET", req[0]["url"]).headers["Set-Cookie"]

h = updateCookie(req[1],cookie)

#Segundo request anexando cookie recibida.
res = requests.request("GET", req[1]["url"], headers=h)

print(res.headers)
