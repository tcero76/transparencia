from funciones import updateHeader, getCookieAndViewState, clickPanel1
from bs4 import BeautifulSoup
import requests

# Solicitud inicial donde se captura la cookie
ViewState, cookie, soup = getCookieAndViewState()

panel1= []
for i in soup.select("a.dor_org_no_senialado"):
    panel1.append({"nombre": i.text, "name" : i["name"] })

ress = []
for item in panel1:
    soup2, click, h = clickPanel1(cookie, ViewState, item)
    panel2 = []
    for i in soup2.select("a.dor_organismos_selecc.Class_id_link_org_link"):
        panel2.append({
            "nombre":i.text,
            "name": i["name"]
        })
    print(panel2)

    for panel in panel2:
        url = (soup.select("form#A3684:form")[0]["action"])
        form = updateHeader(click,ViewState,panel["name"])
        res = requests.request("POST", url , headers=h, data=form)
        soup3 = BeautifulSoup(res.text,"html5lib")
        ress.append(res)
        print(soup3.select("a.btn.btn-default.btn-block.active.estilo_info_ta")[0]["href"])
        print(soup3.select("a.btn.btn-default.btn-block.active.estilo_info_ta")[0].text)

