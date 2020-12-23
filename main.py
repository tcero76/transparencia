from funciones import readRequest, updateCookie, updateViewState
from bs4 import BeautifulSoup
import requests

# Captura desde Chrome con la serie de requests en formato HAR
req = readRequest()
from urllib.parse import quote_plus

# Solicitud inicial donde se captura la cookie
response = requests.request("GET", req[0]["url"])
cookie = response.headers["Set-Cookie"]
soup = BeautifulSoup(response.text,"html5lib")
ViewState= quote_plus(soup.select("#javax.faces.ViewState")[0]["value"])

click = list(r for r in req if r["method"]=="POST")[0]
h = updateCookie(click,cookie)
form = updateViewState(click,ViewState)
res = requests.request("POST", click["url"], headers=h, data=form)
print(res.text)

# soup = BeautifulSoup(res.text,"lxml")
# print(soup.select(".dor_organismos_panel"))
