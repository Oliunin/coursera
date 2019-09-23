import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
ix=0
isum=0
url=('http://py4e-data.dr-chuck.net/comments_288322.xml')
xml = urllib.request.urlopen(url, context=ctx).read()
comments=ET.fromstring(xml)
xlist=comments.findall("comments/comment")
print('length:',len(xlist))
for item in xlist:
    #print("name",item.find('name').text)
    #print('count',item.find('count').text)
    sx=item.find('count').text
    ix=int(sx)
    print(ix)
    isum=isum+ix
print(isum)
