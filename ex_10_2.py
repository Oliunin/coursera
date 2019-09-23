#Посчитать письма в час, отсортировать по возрастанию часов
fh = open("mbox-short.txt")
count = 0
llist=list()
rlist=list()
lline=list()
dhour=dict()
for line in fh:
    if line.startswith("From "):
        stime=line.find(':')
        shour=line[stime-2:stime]
        llist.append(line[stime-2:stime])
for shour in llist:
    dhour[shour]=dhour.get(shour,0)+1
for k,v in dhour.items():
    newtup=(k,v)
    rlist.append(newtup)
    rlist=sorted(rlist)
for k,v in rlist:
    print(k,v)
