import requests as req

def getWebPageHTML(url):
    """
        If I wanted to be an official programmer, I would like
        validate the url (among other things)
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    resp = req.get(url, headers=headers)
    return {"content": resp.text}
