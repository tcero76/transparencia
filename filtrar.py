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