from funciones import readRequest, updateCookie
from bs4 import BeautifulSoup
import requests

# Captura desde Chrome con la serie de requests en formato HAR
req = readRequest()

# Solicitud inicial donde se captura la cookie

response = requests.request("GET", req[0]["url"])
cookie = response.headers["Set-Cookie"]
soup = BeautifulSoup(response.text,"html5lib")
ViewState= soup.select("#javax.faces.ViewState")[0]["value"]

# for r in req:
# # incorpora la cookie en el header de nueva request
#     h = updateCookie(r,cookie)
# #Serie de requests.
#     requests.request("GET", r["url"], headers=h)


# click = list(r for r in req if r["method"]=="POST")[0]
# h = updateCookie(click,cookie)
# res = requests.request("POST", click["url"], headers=h, data=click["postData"])
# print(res.text)
# soup = BeautifulSoup(res.text,"lxml")
# print(soup.select(".dor_organismos_panel"))
# print(res.headers)