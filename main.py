from filtrar import readRequest
import requests

req = readRequest()

#Primer request
cookie = requests.request("GET", req[0]["url"]).headers["Set-Cookie"]

#Crear header nuevo
h = {}
for header in req[1]["headers"]:
    cookieFlag = False
    if header["name"] == "Cookie":
        cookieFlag = True
        h["Cookie"] = cookie
    else:
        h[header["name"]] = header["value"]
    if not(cookieFlag):
        h["Cookie"] = cookie

#Segundo request anexando cookie recibida.
res = requests.request("GET", req[1]["url"], headers=h)

print(res.headers)
