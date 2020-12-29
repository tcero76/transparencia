from funciones import readRequest, updateCookie, updateHeader
from bs4 import BeautifulSoup
import requests

# Captura desde Chrome con la serie de requests en formato HAR
req = readRequest()

# Solicitud inicial donde se captura la cookie
response = requests.request("GET", req[0]["url"])
cookie = response.headers["Set-Cookie"]
soup = BeautifulSoup(response.text,"html5lib")

ViewState= soup.select("input#javax.faces.ViewState")[0]["value"]

# source = "A3684:form:j_idt11:3:j_idt15" #Consejo de defensa del estado
# source = "A3684:form:j_idt11:2:j_idt13" #Congreso de nacional

panel1= []
for i in soup.select("a.dor_org_no_senialado"):
    panel1.append({"nombre": i.text, "name" : i["name"] })

ress = []
for panel in panel1:
    click = list(r for r in req if r["method"]=="POST")[0]
    h = updateCookie(click,cookie)
    form = updateHeader(click,ViewState,panel["name"])
    res = requests.request("POST", click["url"], headers=h, data=form)
    soup = BeautifulSoup(res.text,"html5lib")

    panel2 = []
    for i in soup.select("a.dor_organismos_selecc.Class_id_link_org_link"):
        panel2.append({"nombre":i["name"], "name": i.text})

    for panel in panel2:
        url = (soup.select("form#A3684:form")[0]["action"])

        form = updateHeader(click,ViewState,panel["name"])
        res = requests.request("POST", url , headers=h, data=form)
        soup = BeautifulSoup(res.text,"html5lib")
        print(res.text)
        ress.append(res)
# print(soup.select("div.enlace_ficha_org"))
