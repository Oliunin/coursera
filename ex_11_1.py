import re
fh = open("regex_sum_42.txt")
idig=0
isum=0
ilist=list()
for line in fh:
    sdig=re.findall('[0-9]+', line)
    print(sdig)
    for x in sdig:
        idig=int(x)
        ilist.append(idig)
for y in ilist:
    isum=isum+y
print(isum)
