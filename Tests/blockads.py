import re


def blockads(route, request):
    if re.search(r"(doubleclick|googlesyndication|googleadservices|adservice|amazon-adsystem)", request.url, re.I):
        route.abort()
        #print("successfully aborted an ad")
    else:
        route.continue_()
