#THAT WAS REALY DIFFICULT
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
dcount=7
pos=18
url=None
while dcount > 0:
    if url is None: url=('http://py4e-data.dr-chuck.net/known_by_Bena.html')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    tag=tags[pos-1]
    url=tag.get('href', None)
    name=tag.contents[0]
    print(name)
    dcount=dcount-1
