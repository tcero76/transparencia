from funciones import getCookieAndViewState, clickPanel1


# Solicitud inicial donde se captura la cookie
ViewState, cookie, soup = getCookieAndViewState()
soup2, res  =clickPanel1(cookie, ViewState)
for item in soup2.select("a.org-dir"):
    print(item["href"])

