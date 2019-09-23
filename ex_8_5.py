#вывести список отправителей e-mail
fh = open("mbox-short.txt")
count = 0
llist=list()
lline=list()
for line in fh:
    if line.startswith("From:"):
        lline=line.split()
        llist.extend(lline[1:2])
        count=count+1
for x in llist: print(x)
print("There were", count, "lines in the file with From as the first word")
