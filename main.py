from filtrar import readRequest

import requests

r = readRequest()

# print(r["log"]["entries"][0]["request"])

serie = r["log"]["entries"]
req = []
for request in serie:
    if "https://www.portaltransparencia.cl/PortalPdT/web/guest/directorio-de-organismos-regulados" in request["request"]["url"]:
        req.append(request["request"])

res = requests.request("GET", req[0]["url"])

cookie = res.headers["Set-Cookie"]

print(cookie)
