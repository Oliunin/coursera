#кто отправил больше писем
fh = open("mbox.txt")
count = 0
llist=list()
lline=list()
demail=dict()
for line in fh:
    if line.startswith("From:"):
        lline=line.split()
        llist.extend(lline[1:2])
        count=count+1
for email in llist:
#    print(email)
    demail[email]=demail.get(email,0)+1
bigcount=None
bigemail=None
for email,count in demail.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email
print(bigemail,bigcount)
