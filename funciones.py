import json
import requests
# from bs4 import BeautifulSoup
import urllib

def readRequest():
  with open('./transparencia.json') as f:
    data = json.load(f)
  # Filtrar serie
  serie = data["log"]["entries"]
  req = []
  for request in serie:
    if "https://www.portaltransparencia.cl/PortalPdT/web/guest/directorio-de-organismos-regulados" in request["request"]["url"]:
      req.append(request["request"])
  return req


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

# actualiza el parámetro ViewState en el body de la request
def updateViewState(click,ViewState):
    form = ""
    print(ViewState)
    for i in click["postData"]["text"].split("&"):
        if "javax.faces.ViewState" == i.split("=")[0]:
            form += "javax.faces.ViewState=" + ViewState + "&"
        else:
            form += i.split("=")[0] + "=" + i.split("=")[1] + "&"
    print(len(form))
    return form