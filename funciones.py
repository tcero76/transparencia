import json
from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup

def readRequest():
  with open('./transparencia.json') as f:
    data = json.load(f)
  # Filtrar serie
  return data["log"]["entries"]

def getCookieAndViewState():
    entries = readRequest()
    url = "https://www.portaltransparencia.cl/PortalPdT/buscador-directorio-de-organismos"
    request = list(entrie["request"] for entrie in entries if url in entrie["request"]["url"])
    res = requests.request("GET", request[0]["url"])
    cookie = res.headers["Set-Cookie"]
    soup = BeautifulSoup(res.text, "html5lib")
    ViewState = soup.select("input#javax.faces.ViewState")[0]["value"]
    return ViewState, cookie, soup

def clickPanel1(cookie, ViewState, item=None):
    entries = readRequest()
    request = list(entrie["request"] for entrie in entries if entrie["request"]["method"]=="POST")[0]
    h = updateCookie(request,cookie)
    form = updateViewState(request,ViewState)
    res = requests.request("POST", request["url"], headers=h, data=form)
    soup = BeautifulSoup(res.text,"html5lib")
    return soup, res

#Crear header nuevo
def updateCookie(req, cookie):
  h = {}
  for header in req["headers"]:
      cookieFlag = False
      if header["name"] == "Cookie":
          cookieFlag = True
          h["Cookie"] = cookie
      else:
          h[header["name"]] = header["value"]
      if not(cookieFlag):
          h["Cookie"] = cookie
  return h

def updateViewState(click,ViewState):
    ViewState = quote_plus(ViewState)
    form = ""
    for i in click["postData"]["text"].split("&"):
        if "javax.faces.ViewState" == i.split("=")[0]:
            form += "javax.faces.ViewState=" + ViewState + "&"
        else:
            form += i.split("=")[0] + "=" + i.split("=")[1] + "&"
    return form

# actualiza el parámetro ViewState en el body de la request
def updateHeader(click,ViewState,source):
    source = quote_plus(source)
    ViewState = quote_plus(ViewState)
    form = ""
    for i in click["postData"]["text"].split("&"):
        if "javax.faces.ViewState" == i.split("=")[0]:
            form += "javax.faces.ViewState=" + ViewState + "&"
        elif "javax.faces.source" == i.split("=")[0]:
            form += "javax.faces.source=" + source + "&"
        elif "org.richfaces.ajax.component" == i.split("=")[0]:
            form += "org.richfaces.ajax.component=" + source + "&"
        elif "javax.faces.partial.execute" == i.split("=")[0]:
            form += "javax.faces.partial.execute=" +  source + "&"
        elif "A3684%3Aform%3Aj_idt11%3A3%3Aj_idt15" == i.split("=")[0]:
            form += source + "=" + source + "&"
        else:
            form += i.split("=")[0] + "=" + i.split("=")[1] + "&"
    return form