import urllib.request, urllib.parse, urllib.error
import json

comments=list()
isum=0
url=('http://py4e-data.dr-chuck.net/comments_288323.json')
data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)
vals = list(info.values())
comments=vals[1]
for comment in comments:
    count=comment.get("count")
    isum=isum+count
print(isum)
