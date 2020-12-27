from funciones import readRequest, updateCookie, updateViewState, updateSource
from bs4 import BeautifulSoup
import requests

# Captura desde Chrome con la serie de requests en formato HAR
req = readRequest()

# Solicitud inicial donde se captura la cookie
response = requests.request("GET", req[0]["url"])
cookie = response.headers["Set-Cookie"]
soup = BeautifulSoup(response.text,"html5lib")

ViewState= soup.select("input#javax.faces.ViewState")[0]["value"]

source = "A3684:form:j_idt11:3:j_idt13"
click = list(r for r in req if r["method"]=="POST")[0]
h = updateCookie(click,cookie)
form = updateViewState(click,ViewState)
updateSource(click, source)
res = requests.request("POST", click["url"], headers=h, data=form)

soup = BeautifulSoup(res.text,"html5lib")
print(soup.select("a.dor_organismos_selecc.Class_id_link_org_link")[0]["name"])
